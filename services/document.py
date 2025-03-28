import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from core.vectorstore import create_vectorstore

def configure_retriever(uploaded_files):
    docs = []
    temp_dir = tempfile.TemporaryDirectory()
    
    for file in uploaded_files:
        temp_filepath = os.path.join(temp_dir.name, file.name)
        with open(temp_filepath, "wb") as f:
            f.write(file.getvalue())

        if file.name.endswith(".pdf"):
            loader = PyPDFLoader(temp_filepath)
        elif file.name.endswith(".txt"):
            loader = TextLoader(temp_filepath, encoding="utf-8")
        else:
            continue

        docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500, 
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(docs)
    
    vectordb = create_vectorstore(splits)
    return vectordb.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 2, "fetch_k": 4}
    )