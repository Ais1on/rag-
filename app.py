import streamlit as st
from services.document import configure_retriever
from services.chat import setup_chat_chain
from utils.callback import StreamHandler, PrintRetrievalHandler
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config(page_title="文档问答", page_icon="🦜")
    st.title("🦜 文档问答")

    uploaded_files = st.sidebar.file_uploader(
        label="上传pdf、txt文件",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )

    if not uploaded_files:
        st.info("上传pdf、txt文档后使用")
        st.stop()

    retriever = configure_retriever(uploaded_files)
    qa_chain = setup_chat_chain(retriever)

    if "messages" not in st.session_state or st.sidebar.button("清空聊天记录"):
        st.session_state.messages = [{"role": "assistant", "content": "你好！我是文档问答助手"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("请输入您的问题"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.chat_message("assistant"):
            retrieval_handler = PrintRetrievalHandler(st.container())
            stream_handler = StreamHandler(st.empty())
            
            try:
                response = qa_chain({
                    "question": prompt,
                    "chat_history": st.session_state.messages
                }, callbacks=[retrieval_handler, stream_handler])
                
                answer = response.get("answer", "未获取到有效回答")
                # 确保消息被添加到会话状态
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": answer
                })
                # 显式显示最终答案
                st.markdown(answer)
            except Exception as e:
                st.error(f"请求出错: {str(e)}")
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "抱歉，回答问题出错了"
                })
                stream_handler.on_llm_end(None)  # 强制结束加载状态

if __name__ == "__main__":
    main()