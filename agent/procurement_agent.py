import json

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from agent.inventory_tool import get_inventory_details
from agent.document_tool import search_documents
from agent.business_rules import evaluate_inventory
from agent.ml_tool import predict_stockout
from agent.ml_feature_tool import get_ml_features


# -------------------------------------
# Load LLM
# -------------------------------------

llm = ChatOllama(
    model="llama3.2:3b"
)


# -------------------------------------
# Prompt
# -------------------------------------

prompt = ChatPromptTemplate.from_template(
"""
You are a Senior AI Procurement Analyst.

Use the Business Rule Evaluation and ML Prediction as the PRIMARY source of truth.

Use the retrieved procurement documents ONLY to justify your recommendation.

Never contradict the Business Rules or ML Prediction.

If information is unavailable,
say "Information not available."

Return ONLY valid JSON.

Schema:

{{
    "recommendation":"",
    "priority":"",
    "confidence":"",
    "reason":"",
    "next_action":""
}}

=================================================

{context}

=================================================

User Question:

{question}
"""
)


# -------------------------------------
# Procurement Agent
# -------------------------------------

def procurement_agent(
    sku: str,
    question: str
):

    try:

        # ---------------------------------
        # Inventory
        # ---------------------------------

        inventory = get_inventory_details(sku)

        if inventory is None:

            return {
                "success": False,
                "message": f"SKU '{sku}' not found."
            }

        # ---------------------------------
        # Business Rules
        # ---------------------------------

        business_result = evaluate_inventory(
            inventory
        )

        # ---------------------------------
        # ML Features
        # ---------------------------------

        ml_features = get_ml_features(sku)

        if ml_features is None:

            return {
                "success": False,
                "message": "ML features not found for this SKU."
            }

        # ---------------------------------
        # ML Prediction
        # ---------------------------------

        features = [

            ml_features["weekly_consumption_velocity"],

            ml_features["days_of_supply"],

            ml_features["annual_consumption_value"],

            ml_features["current_stock"]

        ]

        ml_prediction = predict_stockout(
            features
        )

        # ---------------------------------
        # Retrieve Documents
        # ---------------------------------

        documents = search_documents(
            f"""
            SKU : {sku}

            Current Stock :
            {inventory["current_stock"]}

            Reorder Point :
            {inventory["reorder_point"]}

            Safety Stock :
            {inventory["safety_stock"]}

            User Question:

            {question}
            """
        )

        if not documents:

            return {

                "success": False,

                "message": "No relevant documents found."

            }

        document_context = "\n\n".join(

            doc.page_content

            for doc in documents

        )

        # ---------------------------------
        # Context
        # ---------------------------------

        context = f"""

Inventory Information

{inventory}

------------------------------------

Business Rule Evaluation

{business_result}

------------------------------------

ML Features

{ml_features}

------------------------------------

ML Prediction

{ml_prediction}

------------------------------------

Relevant Procurement Documents

{document_context}

"""

        # ---------------------------------
        # Prompt
        # ---------------------------------

        formatted_prompt = prompt.format(

            context=context,

            question=question

        )

        # ---------------------------------
        # LLM
        # ---------------------------------

        response = llm.invoke(
            formatted_prompt
        )

        print("=" * 80)
        print(response.content)
        print("=" * 80)

        # ---------------------------------
        # Parse JSON
        # ---------------------------------

        result = json.loads(
            response.content
        )

        # ---------------------------------
        # Final Response
        # ---------------------------------

        return {

            "success": True,

            "sku": sku,

            "question": question,

            "result": result

        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }