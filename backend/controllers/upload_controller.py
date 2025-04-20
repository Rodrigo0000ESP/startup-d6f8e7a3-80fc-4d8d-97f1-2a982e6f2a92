def process_receipt_upload(image_path):
    try:
        # Extract text from the uploaded image
        extracted_text = extract_text_from_image(image_path)

        # Process the extracted text to structure the data
        structured_data = process_extracted_text(extracted_text)

        # Generate CSV from structured data
        csv_path = 'path/to/generated.csv'
        generate_csv(structured_data, csv_path)

        return {'success': True, 'csv_path': csv_path}
    except Exception as e:
        return {'success': False, 'error': str(e)}