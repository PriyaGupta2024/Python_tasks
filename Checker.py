# palindrome_checker.py

def is_palindrome(s):
    """
    Checks if the given string is a palindrome.
    Ignores case and non-alphanumeric characters.
    """
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

def get_input():
    """
    Prompts the user for a string input.
    Ensures the input is not empty.
    """
    s = input("Enter a string to check if it's a palindrome: ").strip()
    if not s:
        print("Invalid input! Please enter a non-empty string.")
        return None
    return s

def main():
    print("Welcome to the Palindrome Checker Program!")
    while True:
        print("\nMenu:")
        print("1. Check if a string is a palindrome")
        print("2. Exit")

        try:
            choice = int(input("Enter your choice (1-2): "))
        except ValueError:
            print("Invalid choice! Please enter 1 or 2.")
            continue

        if choice == 2:
            print("Thank you for using the program. Goodbye!")
            break

        if choice == 1:
            s = get_input()
            if s is None:
                continue

            if is_palindrome(s):
                print(f"'{s}' is a palindrome!")
            else:
                print(f"'{s}' is not a palindrome.")

        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
