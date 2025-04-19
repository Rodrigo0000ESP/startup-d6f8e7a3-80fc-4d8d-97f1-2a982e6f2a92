filepath: backend/services/ocr_service.py

import pytesseract
from PIL import Image
import csv


def extract_text_from_image(image_path):
    extracted_data = {}
    # Utilize OCR to extract text from image
    extracted_text = pytesseract.image_to_string(Image.open(image_path))
    # Process extracted text to categorize into relevant fields
    # For demonstration purposes, let's assume extracting date and amount
    for line in extracted_text.split('\n'):
        if 'Date' in line:
            extracted_data['date'] = line.split(':')[-1].strip()
        if 'Amount' in line:
            extracted_data['amount'] = line.split(':')[-1].strip()
    return extracted_data


def generate_csv(data, csv_filename):
    # Generate CSV file with extracted data
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

# Example usage:
image_path = 'path/to/your/image.jpg'
extracted_data = extract_text_from_image(image_path)
generate_csv(extracted_data, 'extracted_data.csv')