"""
PDF Text Extractor

This script processes a specified folder containing PDF files, extracting and printing the
text content of each PDF. It demonstrates the use of the PyPDF2 library for reading PDF files
and the os library for directory handling. This script is intended to be used where batch
processing of PDF files for text extraction is required.

Functions:
    extract_text_from_pdf(pdf_file): Extracts text from a specified PDF file.
    process_pdf_folder(folder_path): Processes all PDF files in a given folder, 
    utilizing extract_text_from_pdf.

Usage:
    Run the script with Python 3. Adjust the 'folder_path' variable in the '__main__'
    section to point to the directory containing your PDF files.
"""

import os
import PyPDF2
FOLDER_PATH = 'enrollment_reports'

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a given PDF file.

    Args:
    pdf_file (str): Path to the PDF file.

    Returns:
    str: Extracted text from the PDF.
    """
    text = ""
    try:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(reader.pages):
                print(f'Extracting from page: {page_num}')
                page_text = page.extract_text()
                if page_text:
                    text += page_text
                else:
                    print(f"Warning: No text found on page {page_num} of {pdf_file}")
    except (IOError, PyPDF2.errors.PdfReadError) as e:
        print(f"Error reading file {pdf_file}: {e}")
    return text


def process_pdf_folder():
    """
    Processes all PDF files in a given folder.

    Args:
    folder_path (str): Path to the folder containing PDF files.
    """
    if not os.path.isdir(FOLDER_PATH):
        print(f"Error: The folder {FOLDER_PATH} does not exist.")
        return

    for filename in os.listdir(FOLDER_PATH):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(FOLDER_PATH, filename)
            print(f"Extracting text from {filename}...")
            pdf_text = extract_text_from_pdf(pdf_path)
            if pdf_text:
                print(pdf_text)
            else:
                print(f"No text extracted from {filename}")
            print("\n---\n")

if __name__ == "__main__":
    process_pdf_folder()
