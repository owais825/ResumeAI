from dotenv import load_dotenv
load_dotenv()  # Activate Local Env Vars

import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .title {
        font-size: 2.5em;
        color: #0066cc;
        font-weight: bold;
    }
    .subtitle {
        color: #333;
        font-size: 1.3em;
        margin-bottom: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #e9ecef;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="title">🧠 Resume Analysis using AI</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🚀 Enhance your resume match with job descriptions using the power of Gen AI</p>', unsafe_allow_html=True)
st.divider()

# Tips section
with st.expander("📌 Tips for Using the Application", expanded=True):
    st.markdown("""
    - 📄 **Upload your Resume** (PDF format only).
    - 💼 **Paste Job Description** from job boards.
    - 🔍 **Click the Button** to generate actionable insights powered by Gen AI.
    """)

# Sidebar: Resume Upload
with st.sidebar:
    st.subheader("📄 Upload Your Resume")
    resume = st.file_uploader(label="Upload your resume", type=["pdf"])
    st.info("Only PDF format is supported.")

# Main: Job Description and Analysis
st.subheader("💼 Enter the Job Description")
job_desc = st.text_area(label="Paste Job Description Here", max_chars=10000, height=200, placeholder="E.g. We are looking for a Data Scientist...")

# Button and Output
st.markdown("### 🔍 Analysis")
button = st.button("✨ Get AI Powered Insights")

if button:
    if not resume:
        st.warning("⚠️ Please upload your resume.")
    elif not job_desc.strip():
        st.warning("⚠️ Please paste a job description.")
    else:
        with st.spinner("Analyzing... 🔎"):
            output = profile(resume=resume, job_desc=job_desc)
            st.markdown(output, unsafe_allow_html=True)
