# DocTalk: Convert Documents to Audio and Text


DocTalk is a versatile application that enables users to easily convert different types of documents, including images, PDFs, and Word documents, into both audio files and readable text. With the ability to handle various formats, DocTalk empowers users to consume content through audio or text based on their preferences.

## Features

- **Multi-Format Support:** DocTalk supports several document formats, including image files (PNG, JPG, JPEG), PDFs, and Word documents (docx).
- **Effortless Text Extraction:** The application extracts text from the provided documents, ensuring accurate representation.
- **High-Quality Audio Output:** DocTalk uses the gTTS (Google Text-to-Speech) library to generate high-quality audio output.
- **Interactive User Interface:** The user-friendly interface is built using Streamlit, providing an intuitive experience.
- **Downloadable Outputs:** Users can download extracted text files and audio files (in WAV format) for offline use.

## Getting Started

1. **Clone the Repository:** Clone the DocTalk repository to your local machine:


2. **Install Dependencies:** Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:** Start the application:

    ```bash
    streamlit run app.py
    ```

4. **Access the App:** Open your web browser and go to `http://localhost:8501`.

## Usage

1. **Upload a Document:** Use the provided file uploader to upload documents in supported formats.
2. **Text Extraction:** DocTalk extracts text content from documents, even images, ensuring accessibility.
3. **Read or Listen:** Extracted text is displayed for reading, while the audio player lets you listen to the content.
4. **Download Outputs:** Download extracted text and audio files for offline access using the provided buttons.

## Contributions

Contributions to DocTalk are welcome! If you find issues or have enhancements to suggest, feel free to open issues or pull requests.

## License

This project is licensed under the MIT License. You are free to use and modify the code according to the terms of the license.

## Acknowledgments

DocTalk is built upon the contributions of various open-source libraries, including Streamlit, pytesseract, gTTS, PyPDF2, and python-docx. We extend our gratitude to their creators and contributors.

---

Created by [Your Name](https://github.com/your-username)
