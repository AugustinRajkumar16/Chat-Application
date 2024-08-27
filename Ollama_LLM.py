# Import the supporting Libraries
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Title for your Chatbot
st.title("Chat Bot")

# Input Queries from User-side
input_txt = st.text_input("Please enter your queries here...")

# Check for exit commands
exit_commands = ["close", "exit", "bye", "quit"]

# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Your Name is Augustin's Assistant"),
        ("user", "user query:{query}")
    ]
)

# Initialize the Language model
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

# Process user input
if input_txt:
    # Check if the user input is an exit command
    if input_txt.lower() in exit_commands:
        st.write("Thank you for visiting ! I hope you have a Good Day")
    else:
        # Invoke the chain for normal queries
        response = chain.invoke({"query":input_txt})
        st.write(response)
