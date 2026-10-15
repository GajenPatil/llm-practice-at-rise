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
    input_variables=["content", "customer_name", "agent_name"],
    template="""
You are an AI assistant optimized to write concise, professional, and friendly emails.

Write a professional email to {customer_name}.

Content:
{content}

Signature:
{agent_name}
"""
)

# User Input
content = input("Email content: ")
customer = input("Customer name: ")
agent = input("Agent name: ")

# Create Final Prompt
final_prompt = prompt.format(
    content=content,
    customer_name=customer,
    agent_name=agent
)

# Generate Response
response = llm.invoke(final_prompt)

# Print Output
print("\nGenerated Email:\n")
print(response.content)