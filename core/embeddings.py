from zhipuai import ZhipuAI
import os

class ZhipuAIEmbeddings:
    def __init__(self):
        self.client = ZhipuAI(api_key=os.getenv("ZHIPUAI_API_KEY"))
    
    def embed_documents(self, texts):
        response = self.client.embeddings.create(
            model="embedding-2",
            input=texts
        )
        return [embedding.embedding for embedding in response.data]
    
    def embed_query(self, text):
        response = self.client.embeddings.create(
            model="embedding-2",
            input=[text]
        )
        return response.data[0].embedding