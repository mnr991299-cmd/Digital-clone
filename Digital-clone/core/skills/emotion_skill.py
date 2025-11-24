def can_handle(text):
    # Trigger emotion detection for any personal/emotional message
    keywords = [
        "sad", "upset", "angry", "happy", "depressed", "alone", "stress",
        "stressed", "tired", "worried", "confused", "hurt", "broken",
        "excited", "good mood", "bad mood", "anxious", "anxiety"
    ]
    return any(word in text.lower() for word in keywords)


def handle(text):
    text = text.lower()

    # Emotion detection logic
    if any(word in text for word in ["sad", "depressed", "alone", "hurt", "broken"]):
        return human_emotion(
            "I'm really sorry you're feeling this way. You're not alone — I'm here for you. "
            "Do you want to talk about what made you feel like this?"
        )

    if any(word in text for word in ["angry", "mad"]):
        return human_emotion(
            "I can sense you're angry. It's okay to feel this way. "
            "Take a slow breath. Want to talk about what's bothering you?"
        )

    if any(word in text for word in ["stress", "stressed", "anxiety", "worried"]):
        return human_emotion(
            "It sounds like something is weighing on your mind. "
            "You're doing your best — breathe slowly. Tell me what's stressing you."
        )

    if any(word in text for word in ["tired", "exhausted"]):
        return human_emotion(
            "You've been pushing yourself a lot. It's okay to rest. "
            "Your mind and body deserve a break."
        )

    if any(word in text for word in ["happy", "excited", "good mood"]):
        return human_emotion(
            "That's wonderful! I'm genuinely happy for you. "
            "Tell me what's making you feel so good!"
        )

    # fallback
    return human_emotion("I can feel your emotions. Tell me more — I'm here to listen.")


def human_emotion(text):
    """Make responses feel warm, human and empathetic."""
    variations = [
        text,
        text + "\nYou're stronger than you think.",
        text + "\nI'm right here with you.",
        text + "\nYou can talk to me anytime.",
        text + "\nIt's okay to feel like this.",
    ]

    import random
    return random.choice(variations)