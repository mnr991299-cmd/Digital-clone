import re

def can_handle(text):
    # Remove spaces for easier detection
    clean = text.replace(" ", "")
    # Check if the message contains any math operator
    return any(op in clean for op in ["+", "-", "*", "/"])

def handle(text):
    # Extract only math expressions
    clean = text.replace(" ", "")

    # Only allow numbers, dots and math operators
    if not re.fullmatch(r"[0-9\+\-\*/\.]+", clean):
        return "I can't calculate that."

    try:
        result = eval(clean)
        return f"The answer is {result}"
    except Exception:
        return "I can't calculate that."