import csv_generator
from pytesseract import image_to_string
import cv2

# Load the hotel receipt image
image = cv2.imread('hotel_receipt.jpg')

# Use OCR technology to extract text from the image
extracted_text = image_to_string(image)

# Perform data cleaning and validation on the extracted text
# (Data cleaning and validation code implementation here)

# Format the extracted text into a structured format
# (Text formatting code implementation here)

# Pass the structured text data to the csv_generator for CSV generation
csv_generator.generate_csv(structured_text)