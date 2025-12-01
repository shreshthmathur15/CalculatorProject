# main.py
# Simple Calculator - console based
# Supports: addition, subtraction, multiplication, division
# Author: <Your Name>
# Usage: python main.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid number. Please enter a numeric value.")

def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (×)")
    print("4. Divide (÷)")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in {'1','2','3','4'}:
            print("Invalid choice. Please select 1-5.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            if choice == '1':
                result = add(a, b)
                op = '+'
            elif choice == '2':
                result = subtract(a, b)
                op = '-'
            elif choice == '3':
                result = multiply(a, b)
                op = '×'
            elif choice == '4':
                result = divide(a, b)
                op = '÷'

            print(f"\nResult: {a} {op} {b} = {result}\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
