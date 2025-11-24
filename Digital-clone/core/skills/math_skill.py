def can_handle(text):
    keywords = ["add", "sum", "subtract", "multiply", "divide", "+", "-", "*", "/"]
    return any(k in text for k in keywords)

def handle(text):
    try:
        result = eval(text)
        return f"The answer is {result}"
    except:
        return "I can calculate basic math, try something like: 2+5."