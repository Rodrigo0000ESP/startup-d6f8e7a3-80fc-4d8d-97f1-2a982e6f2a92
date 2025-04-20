import flask
from services.ocr import perform_ocr
from services.csv_generator import generate_csv

app = flask.Flask(__name__)

@app.route('/upload', methods=['POST'])
def handle_upload():
    image_file = flask.request.files['receipt_image']
    text = perform_ocr(image_file)
    if not text:
        return flask.Response('OCR failed', status=422)
    csv_file = generate_csv(text)
    if not csv_file:
        return flask.Response('CSV generation failed', status=422)
    return flask.send_file(csv_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)