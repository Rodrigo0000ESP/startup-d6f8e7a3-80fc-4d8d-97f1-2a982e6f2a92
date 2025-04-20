from flask import Flask, request, jsonify
from services.ocr import extract_text
from services.csv_generator import create_csv

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        text = extract_text(file)
        if text is None:
            return jsonify({'error': 'OCR failed'}), 500
        csv_file = create_csv(text)
        if csv_file is None:
            return jsonify({'error': 'CSV generation failed'}), 500
        return jsonify({'message': 'File processed successfully', 'csv_file': csv_file}), 200