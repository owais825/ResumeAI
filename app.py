from dotenv import load_dotenv
load_dotenv() #Activate the Local Ens Vars

import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

## create the front End.. 
st.header(":blue[Resume Analysis] using AI", divider = "green")
st.subheader("Tips for Using the Application")


## Resume Part

st.sidebar.subheader("Upload the Resume")
resume = st.sidebar.file_uploader(label = "Upload your resume",type=["pdf"])
notes = f'''
* **Upload the Resume**: Please Upload your Resume. This is a GenAI Application.
* **Job Description**: Copy Paste the Job Description from job Boards.
* **Unleash the Power of Gen AI Model**: Click on the Button to generate the Insights.'''
st.write(notes)

## job desc 

st.subheader("Enter ther job Description", divider = True)

job_desc = st.text_area(label="Copy Paste Job Description", max_chars=10000)

button = st.button("Get AI Powered Insights")
if button:
    st.markdown(profile(resume= resume, job_desc=job_desc)) 
