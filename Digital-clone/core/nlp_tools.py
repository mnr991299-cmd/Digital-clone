import random

class NLPTools:
    def tokenize(self, text: str):
        return text.split()

    def sentiment(self, text: str):
        # simple fake sentiment classifier
        words = text.lower()
        if "good" in words or "nice" in words:
            return "positive"
        elif "bad" in words or "sad" in words:
            return "negative"
        return "neutral"