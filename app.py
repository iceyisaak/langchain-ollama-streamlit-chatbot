import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load env variables
load_dotenv()

os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_ENDPOINT']="https://api.smith.langchain.com"


# Prompt Template
prompt=ChatPromptTemplate.from_messages([
    ('system','You are a helpful assistant. Please respond to the customer\'s questions'),
    ('user','Question: {question}')
])

# Streamlit UI
st.title('Langchain Ollama Streamlit Chatbot')
input_text=st.text_input('Please feel free to ask me any questions :)')


# Ollama
llm=Ollama(model='gemma:2b')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))