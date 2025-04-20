from PIL import Image
import pytesseract

# Define the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

# Function to perform OCR on an image file
def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
    return text