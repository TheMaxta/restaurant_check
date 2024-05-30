import os
from openai import OpenAI
from config import OPENAI_API_KEY


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def extract_item_metadata(item_name):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Extract metadata for the restaurant item: {item_name}"
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion