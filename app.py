import streamlit as st
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()
st.title("LLM Chatbot with Groq API")

pdf = st.file_uploader("Upload a PDF file", type=["pdf"], key="file_uploader")
text = ""
if pdf:
    text = "\n".join(page.extract_text() for page in PdfReader(pdf).pages if page.extract_text())

question = st.text_input("Ask me anything!")

if question:
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = f"""
        Answer only from the document provided.
        Document: {text}

        Question: {question}
        """
    st.write(llm.invoke(prompt).content)

