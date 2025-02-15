from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_embedding(chunks: list):
    embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key="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")

    vector_store = FAISS.from_documents(chunks, embedding_model)
    vector_store.save_local("faiss_index")
    return True