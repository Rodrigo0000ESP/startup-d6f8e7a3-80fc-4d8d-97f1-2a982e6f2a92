from backend.services import ocr_service, csv_service


def process_uploaded_file(file):
    extracted_data = ocr_service.extract_data(file)
    categorized_data = categorize_data(extracted_data)
    csv_file = csv_service.generate_csv(categorized_data)
    return csv_file