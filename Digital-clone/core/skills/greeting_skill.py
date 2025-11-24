import random

RESPONSES = [
    "Hey! How can I assist you today?",
    "Hello there! What's up?",
    "Hi! How can I help?",
    "Hey friend, what do you need?",
    "Hello! I'm ready to assist."
]

def can_handle(text):
    text = text.lower()
    return any(word in text for word in ["hi", "hello", "hey","namaste"])

def handle(text):
    return random.choice(RESPONSES)