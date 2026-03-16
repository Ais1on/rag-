# 📝 Simple Vector RAG (简易向量检索增强生成)

这是一个轻量级的**检索增强生成 (RAG, Retrieval-Augmented Generation)** 项目。本项目通过将本地文档向量化并存储到向量数据库中，结合大语言模型（LLM），实现了一个能够“基于本地知识库准确回答问题”的 AI 助手。

## ✨ 特性 (Features)

- **📄 多格式文档支持**: 支持读取 TXT, PDF, Markdown 等格式的本地文档。
- **✂️ 智能文本分割**: 自动将长文档切分为适合大模型处理的文本块 (Chunks)。
- **🔍 向量检索**: 使用向量数据库（如 Chroma / FAISS）进行高效的语义相似度检索。
- **🤖 精准问答**: 结合 LLM，基于检索到的上下文生成准确、不出幻觉的回答。

## 🛠️ 技术栈 (Tech Stack)

* **编程语言**: Python 3.8+
* **核心框架**: LangChain / LlamaIndex
* **大语言模型 (LLM)**: OpenAI GPT-3.5/4 (或替换为通义千问、Kimi、本地 Ollama 等)
* **嵌入模型 (Embeddings)**: OpenAI Embeddings / HuggingFace BGE 模型
* **向量数据库**: ChromaDB / FAISS

## ⚙️ 原理架构 (How it works)

本项目的运行分为两个主要阶段：

1. **数据摄入 (Ingestion)**:
   `读取本地文档` -> `文本分割 (Text Split)` -> `文本向量化 (Embedding)` -> `存入向量数据库`
2. **检索问答 (Retrieval & Generation)**:
   `用户提问` -> `问题向量化` -> `在向量库中检索相似文本` -> `拼接 Prompt 交给 LLM` -> `生成最终回答`

## 🚀 快速开始 (Quick Start)

### 1. 克隆项目
```bash
git clone https://github.com/Ais1on/rag-.git
cd simple-vector-rag
