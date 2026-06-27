from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


#testing
vector = embedding_model.embed_query(
    "Bearing"
)

print(vector)

print(len(vector))