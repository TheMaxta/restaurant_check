# test_ocr.py
from utils.ocr import extract_text_from_image

image_path = 'topchefbill2.jpeg'
text = extract_text_from_image(image_path)
print(text)
