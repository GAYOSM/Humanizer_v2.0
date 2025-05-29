import re
import random

def clean_text(text):
    return ' '.join(text.split())

def synonymize(text):
    # Simple synonym replacement dictionary
    synonyms = {
        "consisting of": ["made up of", "composed of"],
        "contains": ["includes", "holds"],
        "guide": ["lead", "direct"],
        "teachings": ["lessons", "instructions"],
        "stories": ["narratives", "accounts"],
        "laws": ["rules", "principles"],
        "written over centuries": ["compiled over many years", "assembled across generations"],
        "includes": ["features", "contains"],
        "inspires": ["motivates", "encourages"],
        "offering": ["providing", "giving"],
        "connection": ["link", "relationship"],
        "message": ["word", "teaching"],
        "love and salvation": ["compassion and redemption"]
    }
    for key, values in synonyms.items():
        if key in text:
            text = text.replace(key, random.choice(values))
    return text

def format_output(text):
    # Capitalize the first letter of each sentence
    sentences = re.split('([.!?] *)', text)
    formatted = ''.join([s.capitalize() for s in sentences])
    return formatted.strip()

def is_valid_text(text):
    return isinstance(text, str) and len(text) > 0