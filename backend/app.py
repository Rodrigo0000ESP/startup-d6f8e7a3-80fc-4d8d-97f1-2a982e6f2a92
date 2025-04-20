import flask
from routes import upload_receipt

app = flask.Flask(__name__)

# Define route for uploading receipts
@app.route('/upload', methods=['POST'])
def upload_file():
    return upload_receipt.handle_upload_request()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')