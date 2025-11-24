from core.brain import Brain

ai = Brain()

while True:
    user_input = input("You: ")
    response = ai.think(user_input)
    print("AI:", response)