#Import dependency
import streamlit as st
from groq import Groq
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from datetime import datetime
import time
from dotenv import load_dotenv
import os

# loading .env
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.0
)

#setting page configuration (above the link in browser)
st.set_page_config(
    page_title="AI Interview Preparation Agent",
    page_icon="🤖",
    layout="wide"
)

#Creating Sidebar of Application using Streamlit
st.sidebar.title("🤖 AI Career Mentor")

theme = st.sidebar.selectbox(
    "Choose Theme",
    ["Dark", "Light"]
)

effect = st.sidebar.selectbox(
    "Choose Celebration Effect",
    ["Balloons", "Snow"]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    This AI Interview Preparation Agent helps students and job Seekers with:

    ✅ Generate HR, Coding and Technical Questions  
    ✅ Model Answer Generate  
    ✅ Improvement Suggestions  
    ✅ Learning Roadmaps
    ✅ Download PDF Report 
    """
)


if theme == "Dark":

    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

#Creating main page
st.title("Interview Craker 🔥") #Title of the application

st.write(
    "Get personalized Interview  guidance, project ideas, internship suggestions, and learning roadmaps using AI."
)

with st.container():

    st.subheader("Job Seeker Informaton 🌐")

    skills = st.text_input("Tell me Yours Skill : ", placeholder="python, html, SQL etc.")
    Domain = st.selectbox(
            "Select Your Domain",
            ["Computer Science", "Computer Engineering", "AIDS", "Cyber Security", "IT", "Other"]
        )
    
    if Domain == "Other":
            Domain = st.text_input(
                "Enter Your Domain",
                placeholder="Data Science, AI, etc."
            )

    experience = st.radio(
    "What is your experience level?",
    ["Beginner", "Intermediate", "Expert"]
    )

    
    previus_experience = st.text_area(
        "Enter Your Previous Experience (if any)",
        placeholder="Internship at XYZ Company,Projects, etc."
    )

if st.button("🚀 Generate Mock Interview Suggetion"):

    # VALIDATION

    if not skills or not Domain or not experience:

        st.warning("⚠ Please fill all fields.")

    else:

       
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        with st.spinner("AI Agent is analyzing your profile..."):
             
            prompt = f"""
            You are an Professional Interviewer in top company.

            Analyze the job seekker's profile carefully.
            Skills: {skills}
            Domain: {Domain}
            Experience level: {experience}
            Previous Experience and Projects(if any): {previus_experience}

            Provide:

            1. Technical Questions
            2. Coding Questions
            3. HR Questions
            4. Model Answer
            5. Improvemnt Suggestion
            6. Motivation Tip   
  
            Use beginner-friendly and simple language.
            """

            

            response = llm.invoke(prompt)

            answer = response.content

            st.success("✅ Mockk Interview Q&A Generated Successfully!")

            if effect == "Balloons":
                st.balloons()
            else:
                st.snow()

                
                st.subheader("🤖 AI Mentor Response")

                typing_placeholder = st.empty()

                displayed_text = ""

                for char in answer:
                    displayed_text += char
                    typing_placeholder.markdown(displayed_text)
                    time.sleep(0.00)