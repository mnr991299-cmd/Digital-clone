class EmotionEngine:
    def __init__(self):
        self.emotion = "neutral"

    def analyze(self, text: str):
        text = text.lower()
        if any(w in text for w in ["happy", "great", "good"]):
            self.emotion = "happy"
        elif any(w in text for w in ["sad", "bad", "upset"]):
            self.emotion = "sad"
        else:
            self.emotion = "neutral"

        return self.emotion