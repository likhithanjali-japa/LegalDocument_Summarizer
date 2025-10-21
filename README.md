# Legal Document Summarizer

A Python-based tool to automatically summarize PDF documents, combining multiple summarization techniques including Term Frequency, TextRank, Named Entity Recognition (NER), and BERT-based extractive summarization. This project provides both a **Streamlit UI** and a **Jupyter Notebook** interface for advanced analysis.

---

## Features

- Upload PDF documents (including scanned PDFs using OCR)  
- Summarize documents using multiple techniques:  
  - **Term Frequency**  
  - **TextRank**  
  - **NER-based Summarization**  
  - **BERT Extractive Summarization**  
- Generate an **overall summary** combining all methods  
- Display scores and most important sentences  
- Streamlit UI for easy browser-based interaction  

---

## Project Structure

LegalDocument_Summarizer/
├── run.py # Streamlit UI for PDF summarization
├── main.ipynb # Notebook for advanced summarization analysis
├── index.html # Frontend HTML (optional web interface)
├── style.css # Frontend styling
├── requirements.txt # Python dependencies
└── README.md

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/likhithanjali-japa/LegalDocument_Summarizer.git
cd LegalDocument_Summarizer
Create a virtual environment (optional but recommended)


python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies

pip install -r requirements.txt
Download spaCy English model


python -m spacy download en_core_web_sm
Download NLTK datasets


import nltk
nltk.download('punkt')
nltk.download('stopwords')
Install Tesseract OCR (for scanned PDFs)

Windows: Tesseract OCR

Add Tesseract path to system environment variables

Usage
1. Streamlit UI
Run the Streamlit application:


streamlit run run.py
Open the browser at http://localhost:8501

Upload a PDF file

Click Summarize to view the summary

2. Jupyter Notebook Analysis
Open main.ipynb in Jupyter Notebook or Jupyter Lab

Modify the file_path variable to point to your PDF

Run all cells to generate:

Term Frequency summary
TextRank summary
NER summary
BERT-based summary

Overall summary and important sentences
Sentence occurrence analysis


Dependencies:
Python 3.10+
Streamlit
PyPDF2
pdfplumber
pytesseract
Sumy
NLTK
spaCy
NetworkX
scikit-learn




