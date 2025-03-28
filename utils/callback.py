from langchain.callbacks.base import BaseCallbackHandler
import streamlit as st

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text
        self.run_id_ignore_token = None

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

    def on_llm_end(self, response, **kwargs):
        # 移除 self.container.empty() 避免清空消息
        self.container.markdown(self.text)
        self.text = ""
        # 确保UI状态更新完成
        self.container.empty()

class PrintRetrievalHandler(BaseCallbackHandler):
    def __init__(self, container):
        self.container = container
        self.status = None

    def on_retriever_start(self, serialized: dict, query: str, **kwargs):
        self.status = self.container.status("**正在检索上下文**")
        self.status.write(f"**问题:** {query}")

    def on_retriever_end(self, documents, **kwargs):
        if self.status:
            self.status.update(label="检索完成", state="complete")