import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_item_metadata(item_name):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract metadata for the restaurant item: {item_name}",
        max_tokens=50
    )
    return response.choices[0].text.strip()
