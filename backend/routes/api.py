import pytesseract
from PIL import Image

# Preprocess image
def preprocess_image(image_path):
    image = Image.open(image_path)
    gray_image = image.convert('L')
    resized_image = gray_image.resize((300, 300))
    # Adjust contrast if needed
    
    return resized_image

# Apply OCR using Pytesseract
def apply_ocr(image_path):
    preprocessed_image = preprocess_image(image_path)
    extracted_text = pytesseract.image_to_string(preprocessed_image)
    cleaned_text = ' '.join(extracted_text.split())
    return cleaned_text

# Pass the cleaned text to csv_generator module
def process_image(image_path):
    cleaned_text = apply_ocr(image_path)
    csv_generator.generate_csv(cleaned_text)