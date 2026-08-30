# LangGraph Agentic RAG Assistant

An AI-powered conversational assistant built using **LangGraph, LangChain, RAG, tool calling, SQLite, and Streamlit**.

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

## 🛠️ Tech Stack

- **Python**
- **LangGraph**
- **LangChain**
- **FAISS**
- **Streamlit**
- **SQLite**
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
LANGCHAIN_API_KEY=your_key
```

> Never commit your `.env` file or API keys to GitHub.

### 5. Run the application

```bash
streamlit run streamlit_rag_frontend.py
```

## 🎯 Project Goal

This project was built to explore practical implementation of **agentic workflows, RAG, tool calling, persistent memory, and streaming LLM applications using LangGraph**.
