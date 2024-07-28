import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://localhost:8000/chat"

st.title("RAG Chat Application")

# Create a text input for the user's question
user_input = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_input:
        # Send a POST request to the FastAPI backend
        response = requests.post(API_URL, json={"query": user_input})
        
        if response.status_code == 200:
            data = response.json()
            st.write("Response:")
            st.write(data['response'])
            st.write("Sources:")
            st.write(data['Sources'])
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a question.")