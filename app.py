from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

# Inject modern CSS
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #e6f0ff; /* Light Blue */
        color: #333;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 0.7em 1.5em;
        border-radius: 8px;
        transition: background-color 0.3s ease;
        font-size: 1.1em;
        margin-top: 1em;
    }
    .stButton > button:hover {
        background-color: #45a049;
        cursor: pointer;
    }
    .stTextArea textarea {
        background-color: #f0f4f8;
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 10px;
        font-size: 1em;
    }
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: 700;
        color: #003366;
        margin-bottom: 0.2em;
    }
    .subtitle {
        text-align: center;
        font-size: 1.3em;
        color: #444;
        margin-bottom: 1.5em;
    }
    .section-header {
        font-size: 1.5em;
        font-weight: 600;
        margin-top: 2em;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown('<div class="title">🤖 Resume Analysis using AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Match your resume with job descriptions using Generative AI 🔍</div>', unsafe_allow_html=True)
st.divider()

# Tips Section
with st.expander("💡 Tips for Using This Tool", expanded=True):
    st.markdown("""
    - 📄 **Upload your Resume** (PDF only).
    - 📝 **Paste the Job Description** you want to match against.
    - ⚡ **Click the button** to generate AI-driven insights and feedback.
    """)

# Sidebar for Upload
with st.sidebar:
    st.subheader("📎 Upload Resume")
    resume = st.file_uploader("Choose a PDF resume", type=["pdf"])
    st.caption("Max file size: 10MB")

# Job Description Input
st.markdown('<div class="section-header">💼 Enter the Job Description</div>', unsafe_allow_html=True)
job_desc = st.text_area("Paste Job Description Here", placeholder="E.g. We are looking for a Data Scientist...", height=220, max_chars=10000)

# Submit button
button = st.button("🚀 Get AI-Powered Insights")

if button:
    if not resume:
        st.warning("⚠️ Please upload your resume first.")
    elif not job_desc.strip():
        st.warning("⚠️ Please paste a job description.")
    else:
        with st.spinner("Processing... 🔄"):
            st.markdown(profile(resume=resume, job_desc=job_desc), unsafe_allow_html=True)
