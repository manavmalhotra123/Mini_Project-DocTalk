import streamlit as st
from PIL import Image
from PyPDF2 import PdfFileReader
from docx import Document
from gtts import gTTS
import os

st.title("Document to Audio and Text Converter")

# File upload and format selection
file = st.file_uploader("Upload a file", type=["pdf", "docx", "png", "jpg", "jpeg"])

if file is not None:
    file_extension = file.name.split(".")[-1].lower()

    if file_extension in ["png", "jpg", "jpeg"]:
        # Process image files using pytesseract
        img = Image.open(file)
        extracted_text = pytesseract.image_to_string(img)

    elif file_extension == "pdf":
        # Process PDF files
        pdf_reader = PdfFileReader(file)
        extracted_text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            extracted_text += page.extractText() + "\n"

    elif file_extension == "docx":
        # Process Word documents
        doc = Document(file)
        extracted_text = ""
        for paragraph in doc.paragraphs:
            extracted_text += paragraph.text + "\n"

    # Display extracted text
    st.subheader("Extracted Text")
    st.text(extracted_text)

    # Convert text to audio
    audio_tts = gTTS(extracted_text)

    # Provide audio download link
    st.audio(audio_tts.get_wav_data(), format="audio/wav", start_time=0)

    # Save extracted text as text file
    text_file_path = f"extracted_text.{file_extension}.txt"
    with open(text_file_path, "w") as text_file:
        text_file.write(extracted_text)

    # Save audio as MP3
    audio_file_path = f"audio.{file_extension}.mp3"
    audio_tts.save(audio_file_path)

    # Provide download buttons for text and audio files
    st.markdown(
        f"**Download:** [Text File]({text_file_path}), [Audio File]({audio_file_path})"
    )

    # Download button for extracted text
    st.download_button(
        label="Download Extracted Text",
        data=extracted_text,
        file_name=f"extracted_text.{file_extension}.txt"
    )

    # Download button for audio
    st.download_button(
        label="Download Audio",
        data=audio_tts.get_wav_data(),
        file_name=f"audio.{file_extension}.wav"
    )

    # Remove temporary files after download
    os.remove(text_file_path)
    os.remove(audio_file_path)
