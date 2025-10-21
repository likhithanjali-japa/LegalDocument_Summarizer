import streamlit as st
import PyPDF2
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Function to summarize text
def summarize_text(text, sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return "\n".join(str(sentence) for sentence in summary)

# Streamlit UI
st.title("PDF Document Summarizer")

uploaded_file = st.file_uploader("Select a PDF file", type="pdf")

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Original Text")
    st.text_area("PDF Content", text, height=300)

    if st.button("Summarize"):
        summary = summarize_text(text, sentences_count=5)
        st.subheader("Summary")
        st.text_area("Summary", summary, height=200)
