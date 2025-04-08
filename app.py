import streamlit as st
from transformers import pipeline
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="auto"
)

# Load the summarization model
@st.cache_resource
def load_model():
    return pipeline("summarization", model='t5-base', tokenizer='t5-base', framework='pt')

summarizer = load_model()

# App header with styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #4B8BBE;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        color: #666;
        text-align: center;
        margin-bottom: 40px;
    }
    .summary-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4B8BBE;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="main-title">📝 AI Text Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Summarize long text into concise and readable content using T5-base Transformers.</div>' , unsafe_allow_html=True)


# Input
input_text = st.text_area("Enter the text you want to summarize:", height=250)

# Button
if st.button("Generate Summary"):
    if input_text.strip():
        with st.spinner("Summarizing... Please wait."):
            summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
            capitalized_summary = summary[0]['summary_text'].strip().capitalize()

        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
        st.markdown(f"**Summary:**<br>{capitalized_summary}", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to summarize.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>Built by Shuvo.</p>",
    unsafe_allow_html=True
)

