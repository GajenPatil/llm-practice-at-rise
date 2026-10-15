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

@tool
def calculator(expression: str):
    """Useful for solving math problems."""
    return str(eval(expression))

# Initialize the LLM
llm = ChatGroq(
    model=MODEL_ID,
    api_key=GROQ_API_KEY
)


math_agent = initialize_agent(
    tools=[calculator],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

while True:
    question = input("Ask: ")

    # Exit condition
    if question.lower() in ["exit", "quit" , "bye" , "goodbye"]:
        print("Goodbye!")
        break

    # Route math expressions to math_agent
    if any(op in question for op in ["+", "-", "*", "/"]):
        print(math_agent.run(question))
    else:
        print(llm.invoke(question).content)

