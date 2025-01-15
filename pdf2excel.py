# Install necessary libraries
!pip install PyPDF2 pandas

import os
import PyPDF2
import pandas as pd
from google.colab import files

# Function to extract text from a single PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Function to process multiple PDFs and save to a CSV
def process_pdfs(pdf_files):
    extracted_data = []
    for pdf_file in pdf_files:
        text = extract_text_from_pdf(pdf_file)
        extracted_data.append({"PDF_File": os.path.basename(pdf_file), "Text": text})

    # Convert extracted data into a DataFrame
    df = pd.DataFrame(extracted_data)
    return df

# Upload PDFs
print("Please upload your PDF files:")
uploaded_files = files.upload()

# Save uploaded files and process them
pdf_paths = []
for filename in uploaded_files.keys():
    with open(filename, "wb") as f:
        f.write(uploaded_files[filename])
    pdf_paths.append(filename)

# Extract text and save to a CSV
extracted_df = process_pdfs(pdf_paths)
csv_filename = "extracted_text.csv"
extracted_df.to_csv(csv_filename, index=False)
print(f"Text extraction complete. Data saved to {csv_filename}.")

# Download the CSV file
files.download(csv_filename)
