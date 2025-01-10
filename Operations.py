# arithmetic_operations.py

def add(a, b):
    """Performs addition."""
    return a + b

def subtract(a, b):
    """Performs subtraction."""
    return a - b

def multiply(a, b):
    """Performs multiplication."""
    return a * b

def divide(a, b):
    """Performs division and handles division by zero."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def get_input(prompt):
    """
    Prompts the user for input and validates that it's a number.
    Returns the input as a float if valid, or None if invalid.
    """
    try:
        value = input(prompt)
        return float(value)
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return None

def main():
    print("Welcome to the Arithmetic Operations Program!")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue
        
        if choice == 5:
            print("Thank you for using the program. Goodbye!")
            break

        if choice < 1 or choice > 5:
            print("Invalid choice! Please select a valid option.")
            continue

        # Get inputs for the operation
        num1 = get_input("Enter the first number: ")
        if num1 is None:
            continue
        
        num2 = get_input("Enter the second number: ")
        if num2 is None:
            continue

        # Perform the selected operation
        if choice == 1:
            result = add(num1, num2)
            print(f"The result of addition is: {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"The result of subtraction is: {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"The result of multiplication is: {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"The result of division is: {result}")

if __name__ == "__main__":
    main()
