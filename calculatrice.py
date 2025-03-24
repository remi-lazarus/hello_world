def calculatrice(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

if __name__ == "__main__":
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
        operator = input("Enter the operator (+, -, *, /): ")
        result = calculatrice(a, b, operator)
        print("Result:", result)
    except ValueError:
        print("Error: Invalid input")
