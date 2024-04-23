import streamlit as st
from gemini import GeminiClient

# Initialize Gemini API client (replace 'your_api_key' with your actual Gemini API key)
gemini_client = GeminiClient(api_key='AIzaSyDLUSB3mRVTFOhM7WO2vQGf5nh6a8hmNj0')

def summarize_event(content):
    # Assuming 'summarize_text' is a method provided by the Gemini NLP API
    summary = gemini_client.summarize_text(content)
    return summary

st.title('Event Summarizer App')

# User uploads text file or inputs text manually
uploaded_file = st.file_uploader("Upload a file", type=["txt"])
if uploaded_file is not None:
    content = uploaded_file.getvalue().decode("utf-8")
else:
    content = st.text_area("Or paste text here")

if st.button('Summarize'):
    if content:
        summary = summarize_event(content)
        st.write('Summary:')
        st.write(summary)
    else:
        st.write("Please upload a file or paste text to summarize.")
