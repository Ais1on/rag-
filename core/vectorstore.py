from langchain_chroma import Chroma
from core.embeddings import ZhipuAIEmbeddings
import os

def create_vectorstore(documents):
    embeddings = ZhipuAIEmbeddings()
    # 添加持久化路径
    persist_dir = os.path.join(os.path.dirname(__file__), "chroma_db")
    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_dir  # 添加持久化配置
    )