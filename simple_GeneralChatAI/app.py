import os
import streamlit as st
from decouple import config

from langchain.llms import OpenAI

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = config("OPEN_AI_SECRET_KEY")

st.title("GiftDotCom AI Chatbot")

query = st.text_input("What Do You Want From Me Today: ", value="", max_chars=1000, key=None, type="default")

# Llms - Language Learning Management System (This is the name of the AI)
llm = OpenAI(temperature=0.9)

# Generate response
if query:
    response = llm(prompt=query)
    st.write(response)