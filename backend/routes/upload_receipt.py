from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from backend.controllers.upload_controller import process_receipt_image

upload_receipt_blueprint = Blueprint('upload_receipt', __name__)

@upload_receipt_blueprint.route('/upload', methods=['POST'])
def upload():
    if 'receipt' not in request.files:
        return jsonify({'error': 'No receipt part'}), 400
    file = request.files['receipt']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = '/path/to/save/' + filename
        file.save(file_path)
        process_receipt_image(file_path)
        return jsonify({'message': 'Receipt uploaded and processing started'}), 202
