import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=st.secrets("GEMINI_API_KEY"),
    temperature=0.7
)

def generate_summary(name, address, rating):
    prompt = f"Write a very short and with some suggestions of coffee paragraph about a coffee's shop named '{name}',located in 📍 '{address}'convert lan and lat in to street name, which has a rating of ⭐ {rating} if possable write a random user review of one."
    messages = [HumanMessage(content=prompt)]
    response = llm(messages)
    return response.content
