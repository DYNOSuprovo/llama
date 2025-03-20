import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Prompt setup
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You translate english to japanese and add part by part translation so thaat the learner can learn properly, direct translate no other explanation just translate"),
        ("user", "Question:{question}")
    ]
)

# Streamlit UI setup
st.title("Langchain Demo With LLama3")
input_text = st.text_input("What is your question?")

# Initialize Ollama model with correct syntax
llm = Ollama(model="llama3")  # Ensure this is the correct way to pass the model argument
output_parser = StrOutputParser()

# Define chain
chain = prompt | llm | output_parser

# Execute chain if input is pr