from langchain_community.chat_models import ChatOllama
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType

# Tool
@tool
def calculator(expression: str):
    """Useful for solving math problems."""
    return str(eval(expression))

# Local LLM via Ollama
llm = ChatOllama(
    model="llama3"
)

# Agent
agent = initialize_agent(
    tools=[calculator],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.run(" What is 25 * 12? ")
print(response)