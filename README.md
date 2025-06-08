# GPT-Powered PDF Summarizer

This is a simple tool that summarizes the contents of PDF files using OpenAI's GPT models. Built with Python and Streamlit, it provides a quick way to extract and understand the key points of any document.

## Features

- Upload a PDF and receive a concise summary
- Uses GPT API for high-quality summarization
- Clean interface built with Streamlit
- Organizes files into input and output folders

## Tech Stack

- Python 3.10+
- Streamlit
- OpenAI API
- PyPDF2
- python-dotenv

## Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/yourusername/pdf-gpt-summarizer.git
cd pdf-gpt-summarizer
pip install -r requirements.txt
OPENAI_API_KEY=your-api-key-here/ OpenRouter
streamlit run app.py
pdf-gpt-summarizer/
├── app.py
├── requirements.txt
├── .env (not included in GitHub)
├── utils/
│   ├── extract_text.py
│   └── summarize.py
├── input_pdfs/
├── summary_outputs/

