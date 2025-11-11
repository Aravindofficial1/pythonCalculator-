# 🔢 Python Calculator with Smart Choice Input + History

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Store calculation history
history = []

def show_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1/2/3/4/5/6 or name): ").strip().lower()

    # Accept both numbers and words
    if choice in ['6', 'exit', 'quit', 'q']:
        print("👋 Exiting calculator. Goodbye!")
        break

    elif choice in ['5', 'history', 'view']:
        print("\n📜 --- Calculation History ---")
        if not history:
            print("No calculations yet.")
        else:
            for i, h in enumerate(history, start=1):
                print(f"{i}. {h}")
        continue

    elif choice in ['1', 'add', '+']:
        operation = 'add'
    elif choice in ['2', 'subtract', '-', 'minus']:
        operation = 'subtract'
    elif choice in ['3', 'multiply', '*', 'x']:
        operation = 'multiply'
    elif choice in ['4', 'divide', '/', '÷']:
        operation = 'divide'
    else:
        print("❌ Invalid input. Please try again.")
        continue

    # Take numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("⚠️ Please enter valid numbers.")
        continue

    # Perform selected operation
    if operation == 'add':
        result = add(num1, num2)
        text = f"{num1} + {num2} = {result}"
    elif operation == 'subtract':
        result = subtract(num1, num2)
        text = f"{num1} - {num2} = {result}"
    elif operation == 'multiply':
        result = multiply(num1, num2)
        text = f"{num1} × {num2} = {result}"
    elif operation == 'divide':
        result = divide(num1, num2)
        text = f"{num1} ÷ {num2} = {result}"

    print(f"✅ Result: {result}")
    history.append(text)

