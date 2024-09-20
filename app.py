import streamlit as st
import torch


from transformers import pipeline
import pandas as pd

pipe = pipeline('summarization', model='bert_samsum_model_1')
gen_kwargs = {'length_penalty': 0.8, 'num_beams': 8, "max_length": 128}

# Create a Streamlit app
st.title("Document Summarizer")
st.write("Upload a document to generate a summary:")

# Create a file uploader
uploaded_file = st.file_uploader("Choose a file:", type=["txt", "pdf", "docx"])

# Create a button to generate the summary
if st.button("Generate Summary"):
    if uploaded_file is not None:
        # Read the uploaded file
        file_text = uploaded_file.read().decode("utf-8")

     

       

       
        summary_text=pipe(file_text, **gen_kwargs)
       
        text = summary_text[0]["summary_text"]

        # Display the summary
        st.write("Summary:")
        st.write(text)
    else:
        st.write("Please upload a file to generate a summary.")