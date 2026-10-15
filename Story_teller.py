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
    input_variables=["language",
                     "content", 
                     "Story_type", 
                     "audience", 
                     ],
    template="""
You are an AI assistant optimized to tell stories in a concise, professional, funny and engaging manner.

Write a {Story_type} story for {audience}.

Content:
{content}

language:
{language}
"""
)

# User Input
language = input("Story Language: ")
content = input("Story content: ")
story_type = input("Story type: ")
audience = input("Target audience: ")

# Create Final Prompt
final_prompt = prompt.format(
    language=language,
    content=content,
    Story_type=story_type,
    audience=audience
)

# Generate Response
response = llm.invoke(final_prompt)

# Print Output
print("\nGenerated Story:\n")
print(response.content)