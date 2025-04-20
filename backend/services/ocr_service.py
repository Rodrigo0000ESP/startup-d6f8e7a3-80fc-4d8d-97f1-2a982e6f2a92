import cv2
import pytesseract
from google.cloud import vision
from google.cloud.vision_v1 import types

# Initialize the Google Cloud Vision client
google_vision_client = vision.ImageAnnotatorClient()


def extract_text_from_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to Google Cloud Vision Image type
    google_image = types.Image(content=cv2.imencode('.jpg', image)[1].tobytes())

    # Perform text detection using Google Cloud Vision API
    response = google_vision_client.text_detection(image=google_image)
    annotations = response.text_annotations

    # If no annotations, try pytesseract
    if len(annotations) == 0:
        text = pytesseract.image_to_string(image)
    else:
        text = annotations[0].description

    return text
