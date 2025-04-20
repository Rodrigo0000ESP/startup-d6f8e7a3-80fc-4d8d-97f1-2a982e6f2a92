def process_receipt_image(image):
    extracted_text = ocr_service.extract_text(image)
    structured_data = generate_csv_data(extracted_text)
    return structured_data

@app.route('/process_receipt', methods=['POST'])
def process_receipt():
    image = request.files['image']
    structured_data = process_receipt_image(image)
    return Response(structured_data, mimetype='text/csv')