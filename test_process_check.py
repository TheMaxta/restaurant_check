from main import process_check
import json

# Ensure this path points to your actual test image file
image_path = 'topchefbill2.jpeg'

# Process the check with 18% tip and split between 4 people
check = process_check(image_path, tip_percentage=18, num_people=4)

# Print the result
print(json.dumps(check.dict(), indent=2))
