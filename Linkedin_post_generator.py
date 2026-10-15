from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.0
)

# Prompt Template
prompt = PromptTemplate(
    input_variables=["content", "audience", "tone", "length"],
    template= """
You are an AI LinkedIn post generator optimized to write concise, professional, and engaging posts.

Content:
{content}

Audience:
{audience}

Tone:
{tone}

Length:
{length}
"""
)

# User Input
content = input("LinkedIn post content: ")
audience = input("Target audience: ")
tone = input("Desired tone: ")
length = input("Preferred length: ")

# Create Final Prompt
final_prompt = prompt.format(
    content=content,
    audience=audience,
    tone=tone,
    length=length
)

# Generate Response
response = llm.invoke(final_prompt)

# Print Output
print("\nGenerated LinkedIn Post:\n")
print(response.content)