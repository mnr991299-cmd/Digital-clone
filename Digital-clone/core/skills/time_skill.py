from datetime import datetime

def can_handle(text):
    text = text.lower()
    return ("time" in text or "date" in text or "day" in text)

def handle(text):
    now = datetime.now()

    if "time" in text:
        return now.strftime("The current time is %I:%M %p")

    if "date" in text:
        return now.strftime("Today's date is %d-%m-%Y")

    if "day" in text:
        return now.strftime("Today is %A")

    return "I can tell the time or date if you ask!"