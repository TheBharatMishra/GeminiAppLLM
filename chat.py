from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables.

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
## function to load gemini pro model and get response.
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text