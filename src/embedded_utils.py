from langchain_community.embeddings import HuggingFaceEmbeddings

print("INFO: Loading embedding model utility...")

def get_embedding_model(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": 'cuda'},  # Use 'cuda' if you have a GPU
    encode_kwargs={'normalize_embeddings': False}
):
    print(f"INFO: Initializing HuggingFaceEmbeddings model: {model_name}")
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embeddings