1. Receive a hotel receipt image through an HTTP POST request.
2. Use the OCR functionality from 'backend/services/ocr.py' to extract text from the image.
3. Clean and format the extracted text to remove unwanted characters or spaces.
4. Pass the cleaned text to the CSV generation logic in 'backend/services/csv_generator.py' for organization into CSV format.
5. Return the structured CSV data.