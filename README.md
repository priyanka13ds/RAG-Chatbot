
# 📄 RAG Chatbot (Fully Local)

A **fully local Retrieval-Augmented Generation (RAG) chatbot** that answers questions based on custom documents using **local embeddings, FAISS vector search, and a local LLM** — no external APIs, no cloud dependency.

---

## 🚀 Features

* 📑 PDF document ingestion
* ✂️ Text chunking for efficient retrieval
* 🔢 **Local embeddings** using HuggingFace Sentence Transformers
* 📦 Vector search with **FAISS**
* 🤖 **Fully local LLM** using Ollama (Mistral)
* 💬 Conversational memory
* 🌐 Interactive UI with Streamlit
* 🔒 Works **offline**, no API keys required

---

## 🧠 Architecture Overview

```
PDF Documents
     ↓
Text Chunking
     ↓
Local Embeddings (Sentence-Transformers)
     ↓
FAISS Vector Store
     ↓
Retriever
     ↓
Local LLM (Ollama - Mistral)
     ↓
Streamlit Chat Interface
```

---

## 🛠️ Tech Stack

* **Python 3.11**
* **LangChain**
* **HuggingFace Sentence Transformers**
* **FAISS**
* **Ollama (Mistral LLM)**
* **Streamlit**

---

## 📁 Project Structure

```
rag-chatbot/
│── app.py              # Streamlit chatbot UI
│── ingest.py           # Document ingestion & vector creation
│── requirements.txt    # Python dependencies
│── README.md
│── .gitignore
│── data/
│   └── sample.pdf      # Input document
│── vectorstore/        # FAISS index (generated)
│── venv/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Your Document

Place your PDF inside the `data/` folder and rename it to:

```
sample.pdf
```

---

### 5️⃣ Create Vector Store (Local Embeddings)

```bash
python ingest.py
```

You should see:

```
✅ Vector store created successfully!
```

---

### 6️⃣ Install Ollama (Local LLM)

Download and install Ollama:
👉 [https://ollama.com/download](https://ollama.com/download)

Pull the Mistral model:

```bash
ollama pull mistral
```

---

### 7️⃣ Run the Chatbot

```bash
streamlit run app.py
```

Open the browser and start asking questions about your document.

---

## 💡 Example Questions

* “What is this document about?”
* “Summarize the key points”
* “Explain this concept in simple terms”
* “What are the conclusions?”

---

## 🔮 Future Enhancements

* Source citation display
* Multi-PDF support
* Chat history UI
* Dockerization
* FastAPI backend

---

