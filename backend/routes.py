from flask import Flask, request
from .controllers.upload_controller import UploadController

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'receipt' in request.files:
        file = request.files['receipt']
        return UploadController.handle_receipt_upload(file)
    else:
        return 'No file part', 400

@app.route('/correct', methods=['POST'])
def correct_data():
    data = request.get_json()
    return UploadController.handle_data_correction(data)

# Additional routes for other functionalities can be added here

if __name__ == '__main__':
    app.run(debug=True)