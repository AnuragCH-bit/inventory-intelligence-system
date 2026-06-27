from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="rag/vectordb",
    embedding_function=embedding_model
)

retriever = vector_db.as_retriever(
    search_kwargs={
        "k": 3
    }
)

question = "What is the minimum order quantity for bearings?"

results = retriever.invoke(question)

for doc in results:

    print("=" * 60)

    print(doc.page_content)

    print(doc.metadata)