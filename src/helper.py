import fitz  # PyMuPDF
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

MAX_RESUME_BYTES = 5 * 1024 * 1024
MAX_RESUME_CHARACTERS = 30_000


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file: A Streamlit uploaded PDF.
        
    Returns:
        str: The extracted text.
    """
    file_bytes = uploaded_file.getvalue()
    if not file_bytes:
        raise ValueError("The uploaded file is empty.")
    if len(file_bytes) > MAX_RESUME_BYTES:
        raise ValueError("Please upload a PDF smaller than 5 MB.")

    try:
        with fitz.open(stream=file_bytes, filetype="pdf") as document:
            text = "\n".join(page.get_text() for page in document)
    except fitz.FileDataError as error:
        raise ValueError("The uploaded file is not a readable PDF.") from error

    text = text.strip()
    if not text:
        raise ValueError(
            "No selectable text was found. Upload a text-based PDF or use OCR first."
        )
    if len(text) > MAX_RESUME_CHARACTERS:
        raise ValueError("This resume contains too much text. Please upload a shorter PDF.")
    return text


def ask_openai(prompt, max_tokens=500):
    """Send a request to Groq. The name is retained for compatibility."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is missing. Add it to your environment or .env file.")

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_completion_tokens=max_tokens,
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("The AI service returned an empty response. Please try again.")
    return content.strip()
