from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from datetime import datetime
from dotenv import load_dotenv
import os

# Groq Configuration
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("API Key loaded:", GROQ_API_KEY)

MODEL_ID = "llama-3.3-70b-versatile"

# Tool 1 
@tool
def calculator(expression: str) -> str:
    """Useful for solving mathematical expressions."""
    return str(eval(expression))

# Tool 2
@tool
def current_time(dummy: str) -> str:
    """useful for getting the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Initialize the LLM
llm = ChatGroq(
    model=MODEL_ID,
    api_key=GROQ_API_KEY
)

# Initialize the agent with the tools
agent = initialize_agent(
    tools=[calculator, current_time],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example usage
response = agent.run("What is the current time and what is 5 multiplied by 8?")
print(response)