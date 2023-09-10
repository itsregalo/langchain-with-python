import os
import streamlit as st
from decouple import config


from langchain.llms import OpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings # used to make the embeddings (ie. the vectors)

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = config("OPEN_AI_SECRET_KEY")

st.title("GiftDotCom TruthGPT")

query = st.text_input("What Do You Want To Know: ", value="", max_chars=1000, key=None, type="default")

# load my data
loader = DirectoryLoader("data/", glob="*.txt")

documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

texts = text_splitter.split_documents(documents)

# make the embeddings
embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])

documents_search = Chroma.from_documents(texts, embeddings)

llmMe = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])

qa = RetrievalQA.from_chain_type(llm = llmMe, chain_type='stuff', retriever=documents_search.as_retriever())

# ask a question
if query:
    answer = qa.run(query)
    st.write(answer)