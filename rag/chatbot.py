from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from retriever import retriever

llm = ChatOllama(
    model="llama3.2:3b"
)

prompt = ChatPromptTemplate.from_template(
"""
You are an Inventory Procurement Assistant.

Answer ONLY using the provided context.

If the answer is not available in the context,
say:

"I don't have enough information."

Context:
{context}

Question:
{question}

Answer:
"""
)

question = input("Ask your question: ")

documents = retriever.invoke(question)

context = "\n\n".join(
    doc.page_content
    for doc in documents
)

formatted_prompt = prompt.format(
    context=context,
    question=question
)

response = llm.invoke(
    formatted_prompt
)

print("\n")
print("=" * 60)
print(response.content)
print("=" * 60)