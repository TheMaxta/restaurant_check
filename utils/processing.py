from utils.models import Check, Item
from utils.openai_api.py import extract_item_metadata

def create_check_from_text(text):
    items = []
    lines = text.split('\n')
    for line in lines:
        if line.strip():
            parts = line.rsplit(' ', 1)
            if len(parts) == 2 and parts[1].replace('.', '', 1).isdigit():
                name, price = parts
                items.append(Item(name=name.strip(), price=float(price)))
    check = Check(items=items)
    check.total = sum(item.price for item in check.items)
    return check

def add_metadata_to_items(check):
    for item in check.items:
        item.type = extract_item_metadata(item.name)
