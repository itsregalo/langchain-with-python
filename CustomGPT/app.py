import os
import streamlit as st
from decouple import config


from langchain.llms import OpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings # used to make the embeddings (ie. the vectors)

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = config("OPEN_AI_SECRET_KEY")

st.title("GiftDotCom TruthGPT")

query = st.text_input("What Do You Want To Know: ", value="", max_chars=1000, key=None, type="default")

# load my data
loader = DirectoryLoader("data/", glob="*.txt")

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=800, chunk_overlap=200)
documents = text_splitter.split_documents(loader.load())

db = Chroma.from_documents(documents, OpenAIEmbeddings())

# Llms - Language Learning Management System (This is the name of the AI)
llm = OpenAI(temperature=0.9, vector_store=db)

# Generate response
if query:
    response = llm(prompt=query)
    st.write(response)
    