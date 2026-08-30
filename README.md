# LangGraph Agentic RAG Assistant

An AI-powered conversational assistant built using **LangGraph, LangChain, RAG, tool calling, SQLite, Streamlit, and LangSmith**.

The assistant can maintain conversations across threads, answer questions from uploaded PDF documents, and intelligently use different tools when required.

## 🚀 Features

- 🤖 Agentic workflow using **LangGraph**
- 📄 **RAG-based PDF question answering**
- 🔎 Semantic search using **FAISS**
- 🛠️ Tool calling with multiple utilities
- 🌐 Web search
- 🧮 Calculator
- 📈 Stock price lookup
- 💬 Persistent conversation history
- 🧵 Thread-based conversations
- 💾 SQLite checkpointing
- ⚡ Streaming AI responses
- 📊 **LangSmith observability and tracing**
- 🖥️ Streamlit interface

## 🧠 Architecture

```text
                    User
                     │
                     ▼
              Streamlit Frontend
                     │
                     ▼
              LangGraph Agent
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       LLM/RAG     Tools     Memory
          │          │          │
          ▼          ▼          ▼
        FAISS    Web/Calc/   SQLite
                  Stocks
                     │
                     ▼
              LangSmith Tracing
```

## 📄 RAG Pipeline

```text
PDF
 ↓
Document Loader
 ↓
Text Splitting
 ↓
Embeddings
 ↓
FAISS Vector Store
 ↓
Retriever
 ↓
Relevant Context
 ↓
LLM Response
```

Each conversation can maintain its own document context, allowing users to upload a PDF and ask questions about it.

## 📊 Observability with LangSmith

**LangSmith** is integrated into the application for tracing and observability of LangGraph/LangChain execution.

It helps with:

- Monitoring LLM and tool calls
- Tracing agent workflows
- Debugging execution flows
- Analyzing application runs

LangSmith is configured through environment variables without requiring a separate integration module.

## 🛠️ Tech Stack

- **Python**
- **LangGraph**
- **LangChain**
- **FAISS**
- **Streamlit**
- **SQLite**
- **LangSmith**
- **LLM APIs**
- **PyPDF**

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/priyam-sharma909/LangGraph-Agentic-RAG-Assistant.git
cd LangGraph-Agentic-RAG-Assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add the required API keys.

```env
GROQ_API_KEY=your_key
GOOGLE_API_KEY=your_key
HUGGINGFACEHUB_API_TOKEN=your_token

LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=your_langsmith_endpoint
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=your_project_name
```

> Never commit your `.env` file or API keys to GitHub.

### 5. Run the application

```bash
streamlit run streamlit_rag_frontend.py
```

## 🎯 Project Goal

This project was built to explore practical implementation of **agentic workflows, RAG, tool calling, persistent memory, streaming LLM applications, and observability using LangGraph and LangSmith**.
