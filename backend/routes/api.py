from flask import Flask, request, jsonify
import ocr_module
import csv

app = Flask(__name__)

@app.route('/api/hotel_receipt', methods=['POST'])
def extract_data():
    receipt_data = request.data
    extracted_data = ocr_module.extract_data(receipt_data)
    if extracted_data:
        with open('hotel_receipt.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(extracted_data)
        return send_file('hotel_receipt.csv', as_attachment=True)
    else:
        return jsonify({'error': 'Failed to extract data from receipt'})

if __name__ == '__main__':
    app.run()