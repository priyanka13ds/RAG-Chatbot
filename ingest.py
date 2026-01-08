from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_PATH = "data/sample.pdf"
DB_PATH = "vectorstore"

def ingest():
    print("📄 Loading PDF...")
    loader = PyPDFLoader(DATA_PATH)
    documents = loader.load()

    print("✂️ Splitting text...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    print("🔢 Creating LOCAL embeddings (no API, free)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("💾 Creating FAISS vector store...")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_PATH)

    print("✅ Vector store created successfully!")

if __name__ == "__main__":
    ingest()

