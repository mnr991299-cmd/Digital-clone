import random

class ResponseGenerator:

    def generate(self, text: str, emotion: str):

        text = text.lower()

        # 1. Greetings
        greetings = ["hi", "hello", "hey", "namaste", "yo"]
        if any(g in text for g in greetings):
            return random.choice([
                "Hello! How can I assist you today?",
                "Hi! What's on your mind?",
                "Hey there! How can I help?",
            ])

        # 2. If user asks a question
        if text.endswith("?"):
            return random.choice([
                "That's an interesting question!",
                "Let me think about that...",
                "Good question! What do YOU think?",
            ])

        # 3. Emotional responses
        if emotion == "happy":
            return random.choice([
                "That's wonderful to hear! 😊",
                "Awesome! I'm happy for you!",
                "Great vibes! Keep it up!",
            ])

        if emotion == "sad":
            return random.choice([
                "I'm sorry you're feeling that way. 💛",
                "I'm here for you. Want to talk about it?",
                "It’s okay to feel sad. You’re not alone.",
            ])

        # 4. If user expresses confusion
        if "don't know" in text or "confused" in text:
            return "No worries. Tell me what you're confused about."

        # 5. If user asks for help
        if "help" in text:
            return "Sure! Tell me what you need help with."

        # 6. Random fallback (instead of 'tell me more')
        fallback_responses = [
            "Interesting... go on!",
            "Hmm... I'm listening.",
            "Tell me more about that!",
            "Okay! Explain a bit more.",
            "I see. What happened next?",
        ]

        return random.choice(fallback_responses)