from flask import request, jsonify
from backend.services.ocr_service import extract_text_from_image
from backend.services.csv_service import generate_csv

@app.route('/upload', methods=['POST'])
def upload_receipt():
    if 'receipt' in request.files:
        file = request.files['receipt']
        image_path = save_uploaded_file(file)
        extracted_text = extract_text_from_image(image_path)
        parsed_data = parse_receipt_data(extracted_text)
        csv_data = generate_csv(parsed_data)
        return jsonify({
            'status': 'success',
            'data': csv_data
        }), 200
    else:
        return jsonify({'status': 'error', 'message': 'No file part'}), 400

def save_uploaded_file(file):
    # Function to save the uploaded file to the server
    pass

def parse_receipt_data(text):
    # Function to parse the extracted text into structured data
    pass