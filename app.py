import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(page_title="Healthcare RAG Chatbot", layout="centered")
st.title("🩺 Healthcare & Fitness RAG Chatbot")

st.markdown(
    "_This chatbot provides general healthcare and fitness information based on reference documents._  \n"
    "**Disclaimer:** This is for educational purposes only."
)

# -----------------------------
# Session State for Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Load Embeddings (Cached)
# -----------------------------
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

embeddings = load_embeddings()

# -----------------------------
# Load FAISS Vector Store (Cached)
# -----------------------------
@st.cache_resource
def load_vectorstore():
    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

db = load_vectorstore()
retriever = db.as_retriever(search_kwargs={"k": 2})

# -----------------------------
# Local LLM (Mistral via Ollama)
# -----------------------------
llm = Ollama(
    model="mistral",
    temperature=0,
    num_predict=256
)

# -----------------------------
# Prompt Template
# -----------------------------
prompt = PromptTemplate.from_template(
    """You are a healthcare and fitness assistant.
Answer the question using ONLY the context provided.
If the information is not available in the context, say you do not know.
Do not provide medical diagnosis or treatment.

Context:
{context}

Question:
{question}

Answer:
"""
)

# -----------------------------
# RAG Chain (Modern LangChain)
# -----------------------------
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input("Ask a healthcare or fitness-related question")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = rag_chain.invoke(user_input)
            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

