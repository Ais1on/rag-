from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
import os

def setup_chat_chain(retriever):
    msgs = StreamlitChatMessageHistory()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        chat_memory=msgs,
        return_messages=True,
        output_key="answer"  # 明确指定memory的输出键
    )

    llm = ChatOpenAI(
        api_key=os.getenv("MOONSHOT_API_KEY"),
        base_url="https://api.moonshot.cn/v1",
        model="moonshot-v1-8k",
        streaming=True,
        temperature=0.3,
        max_retries=2,
        request_timeout=30
    )

    return ConversationalRetrievalChain.from_llm(
        llm,
        retriever=retriever,
        memory=memory,
        verbose=True,
        return_source_documents=True,
        output_key="answer"
    )