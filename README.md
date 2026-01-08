# 📄 Retrieval-Augmented Generation (RAG) Chatbot

A production-style Retrieval-Augmented Generation (RAG) chatbot for document-grounded question answering.  
This project demonstrates an end-to-end GenAI pipeline using local embeddings, vector search, and a locally hosted large language model to enable efficient, privacy-preserving inference on custom documents.

---

## ⚡ Quick Start (TL;DR)

```bash
git clone https://github.com/priyanka13ds/RAG-Chatbot.git
cd RAG-Chatbot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python ingest.py
ollama pull mistral
streamlit run app.py
```

## Key Features

* PDF-based knowledge ingestion
* Semantic text chunking for improved retrieval
* Local embeddings using HuggingFace Sentence Transformers
* FAISS-based vector similarity search
* Locally hosted LLM via Ollama (Mistral)
* Multi-turn conversational memory
* Interactive Streamlit-based UI
* Fully offline and privacy-preserving inference

---

## 🧠 Architecture Overview

```
User Document (PDF)
        ↓
Text Chunking
        ↓
Sentence Embeddings (Local)
        ↓
FAISS Vector Store
        ↓
Semantic Retriever
        ↓
Local LLM (Ollama – Mistral)
        ↓
Streamlit Chat Interface
```

---

## 🛠️ Technology Stack

- **Language:** Python 3.11  
- **Orchestration:** LangChain  
- **Embeddings:** HuggingFace Sentence Transformers  
- **Vector Store:** FAISS  
- **LLM Runtime:** Ollama (Mistral)  
- **Frontend:** Streamlit  

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

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

---

### 2️⃣ Create and Activate Virtual Environment

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

### 4️⃣ Add Input Document

Place a PDF file inside the data/ directory and rename it to:

```
sample.pdf
```

---

### 5️⃣ Build the Vector Store

Generate embeddings and create the FAISS index:

```bash
python ingest.py
```

Expected output:

```
✅ Vector store created successfully!
```

---

### 6️⃣ Install and Configure Local LLM (Ollama)

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

The application will open in your browser, allowing you to interactively query your document.

---

## 💡 Sample Queries
* What is the main topic of this document?
* Summarize the key points.
* Explain this concept in simple terms.
* What conclusions are presented?

---

## 🎯 Why This Project Matters

This project demonstrates hands-on experience with:

- Retrieval-Augmented Generation (RAG) system design
- Vector similarity search for semantic information retrieval
- Integration of locally hosted large language models for cost-efficient inference
- End-to-end GenAI application development, from data ingestion to user-facing interface

It reflects real-world engineering considerations such as data privacy, reproducibility, and modular system design.

---

## 🔮 Future Enhancements

- Source citation and document traceability  
- Multi-document ingestion and indexing  
- Enhanced chat history visualization  
- Dockerized deployment  
- FastAPI backend for scalable serving  

---

