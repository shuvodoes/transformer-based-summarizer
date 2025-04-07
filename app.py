
import streamlit as st
from transformers import pipeline

# Load the model
@st.cache_resource
# Load the model
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

# Streamlit User interface
st.set_page_config(page_title="Text Summarizer", page_icon="📝", layout="centered")
st.title("✨ Text Summarizer with T5 Transformer.")
st.markdown("""
    Summarize any text in seconds with the T5 Transformer model! Paste articles, emails, or reports, click Summarize, and get a concise version instantly. Save time, capture key ideas—try it now! 
""", unsafe_allow_html=True)

# Adding a custom background color
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f7f7f7;
    }
    .sidebar .sidebar-content {
        background-color: #f7f7f7;
    }
    </style>
    """, unsafe_allow_html=True
)

# Input text area
st.markdown("<h3>📜 Enter Your Text Below</h3>", unsafe_allow_html=True)
input_text = st.text_area("Your text to summarize:", "", height=200)

# Add a nice button
summarize_button = st.button("Summarize", key="summarize_button")
# Generate summary
if summarize_button:
    if input_text.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
            st.subheader("📑 Summary:")
            st.write(summary[0]['summary_text'].capitalize())
    else:
        st.warning("Please! Enter some text to summarize.")

# Optional: Add footer with credits
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 12px; color: grey;'>Made with ❤️ by Shuvo</p>
    """, unsafe_allow_html=True
)
