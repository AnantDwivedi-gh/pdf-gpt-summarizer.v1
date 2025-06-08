import streamlit as st
from utils.extract_text import extract_text_from_pdf
from utils.summarize import get_summary
import os

st.set_page_config(page_title="PDF GPT Summarizer")

st.title("PDF GPT Summarizer")
st.markdown("Upload a PDF and get an AI-generated summary.")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        raw_text = extract_text_from_pdf(uploaded_file)

    st.subheader("🔍 Extracted Text Preview")
    st.text_area("Text from PDF", raw_text[:1000] + "...", height=200)

    if st.button("Generate Summary"):
        with st.spinner("Calling GPT..."):
            summary = get_summary(raw_text)
        
        st.subheader(" Summary")
        st.text_area("AI Summary", summary, height=200)

        output_path = os.path.join("outputs", "summary.txt")
        with open(output_path, "w") as f:
            f.write(summary)
        st.success(f"Summary saved to {output_path}")
