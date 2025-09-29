import google.generativeai as genai
from pdf import read_pdf
import streamlit as st
import os
genai.configure(api_key =os.getenv("GOOGLE-API-KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

## read the pdf
def profile(resume,job_desc):
    if resume is not None:
        resume_doc = read_pdf(resume)
        st.markdown("Resume has been uploaded")
    else:
        st.warning("Resume Missing")
    fit = model.generate_content(f'''Read the resume and job description. Give the candidate friendly, actionable feedback on how well they match and how they can improve.
    
    Job Description:{job_desc}
    Resume:{resume}''')
    ## Return the result
    return(st.write(fit.text))
