from rag.retriever import retriever


def search_documents(question: str):

    documents = retriever.invoke(question)

    return documents