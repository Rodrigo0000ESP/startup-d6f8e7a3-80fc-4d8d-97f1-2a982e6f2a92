import csv_generator
from pytesseract import image_to_string
import cv2

# Receive structured hotel receipt data
def process_hotel_receipt_data(receipt_data):
    # Process the data using OCR technology to extract text
    extracted_text = image_to_string(receipt_data)
    
    # Validate and format the extracted information
    validated_text = validate_extracted_text(extracted_text)
    
    # Generate CSV data with customizable fields
    csv_data = generate_csv(validated_text)
    
    return csv_data