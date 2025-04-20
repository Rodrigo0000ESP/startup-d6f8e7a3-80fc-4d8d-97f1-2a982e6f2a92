def process_hotel_receipt_image(image_path):
    extracted_text = extract_text(image_path)
    if not extracted_text:
        return None
    validated_data = validate_data(extracted_text)
    if not validated_data:
        return None
    csv_data = generate_csv(validated_data)
    return csv_data