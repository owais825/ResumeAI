import google.generativeai as genai
from pdf import read_pdf
import streamlit as st
import os
genai.configure(api_key =os.getenv("GOOGLE_API_1"))

model = genai.GenerativeModel("gemini-2.0-flash")

## read the pdf
def profile(resume,job_desc):
    if resume is not None:
        resume_doc = read_pdf(resume)
        st.markdown("Resume has been uploaded")
    else:
        st.warning("Resume Missing")
    fit = model.generate_content(f'''ACt as a HR or ops head in AI domain and compare {resume} with {job_desc} and suggest - Am I a Good fit?''')
    ## Return the result
    return(st.write(fit.text))
