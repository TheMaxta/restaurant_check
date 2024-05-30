import json
from utils.ocr import extract_text_from_image
from utils.processing import create_check_from_text, add_metadata_to_items
from utils.models import Check

def process_check(image_path, tip_percentage=15, num_people=1):
    # Step 1: Extract text from image
    text = extract_text_from_image(image_path)
    
    # Step 2: Create check object from text
    check = create_check_from_text(text)
    
    # Step 3: Add metadata to items
    add_metadata_to_items(check)
    
    # Calculate tip and split
    check.calculate_tip(tip_percentage)
    check.calculate_split(num_people)
    
    return check

if __name__ == "__main__":
    image_path = 'topchefbill2.jpeg'
    check = process_check(image_path, tip_percentage=18, num_people=4)

    print(json.dumps(check.dict(), indent=2))
