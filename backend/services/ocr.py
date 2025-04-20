import pytesseract
from PIL import Image


def perform_ocr(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale
    text = pytesseract.image_to_string(image)
    cleaned_text = ' '.join(text.split())  # Remove extra spaces
    return cleaned_text

# Example usage:
# cleaned_text = perform_ocr('path/to/image.jpg')