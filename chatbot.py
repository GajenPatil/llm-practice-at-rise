import streamlit as st
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.question_answering import load_qa_chain

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Groq Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_ID = "llama-3.3-70b-versatile"
# Error Handling for Missing API Key
if not GROQ_API_KEY:
    st.error("Error: Groq API key not found.")
    st.info(
        'Please create a .env file in your project directory with GROQ_API_KEY="your_api_key"'
    )
    st.stop()

st.header("My First PDF Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader(
        "Upload a PDF file and start asking questions",
        type="pdf"
    )

# Process PDF
if file is not None:
    pdf_reader = PdfReader(file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )

    chunks = text_splitter.split_text(text)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create vector store
    vector_store = FAISS.from_texts(
        chunks,
        embedding=embeddings
    )

    # User question
    user_question = st.text_input("Type your question here")

    if user_question:
        match = vector_store.similarity_search(user_question)

        # Groq LLM
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=MODEL_ID,
            temperature=0.1
        )

        # QA Chain
        chain = load_qa_chain(
            llm,
            chain_type="stuff"
        )

        response = chain.run(
            input_documents=match,
            question=user_question
        )

        st.write(response)