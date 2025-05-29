import requests

def correct_text(text):
    """
    Uses LanguageTool public API to correct grammar and spelling.
    """
    url = "https://api.languagetool.org/v2/check"
    data = {
        "text": text,
        "language": "en-US"
    }
    response = requests.post(url, data=data)
    result = response.json()
    matches = result.get("matches", [])
    corrected = list(text)
    offset_shift = 0

    for match in matches:
        offset = match["offset"] + offset_shift
        length = match["length"]
        replacements = match["replacements"]
        if replacements:
            replacement = replacements[0]["value"]
            corrected[offset:offset+length] = list(replacement)
            offset_shift += len(replacement) - length

    return "".join(corrected)
