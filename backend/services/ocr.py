```python
import pytesseract
from PIL import Image
import csv


def extract_data_from_receipt(image_path):
    data = {}
    # Use OCR to extract text from the image
    text = pytesseract.image_to_string(Image.open(image_path))
    # Process the extracted text to get relevant data
    # Example: extract date, items, prices
    data['date'] = '20-09-2021'
    data['items'] = ['Item 1', 'Item 2', 'Item 3']
    data['prices'] = ['10.99', '5.00', '8.50']
    return data


def generate_csv(data, csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Item', 'Price'])
        for i in range(len(data['items'])):
            writer.writerow([data['date'], data['items'][i], data['prices'][i]])


# Example usage
image_path = 'receipt.jpg'
extracted_data = extract_data_from_receipt(image_path)
csv_file = 'output.csv'
generate_csv(extracted_data, csv_file)
```