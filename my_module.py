def reverse_text(text):
    return text[::-1]


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"
