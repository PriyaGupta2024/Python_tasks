# file_handling.py

# file_handling.py

def count_words_in_file(filename):
    """
    Counts the number of words in the given file.
    Returns the word count or an error message if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"

def write_word_count(output_filename, word_count):
    """
    Writes the word count to the specified file.
    """
    try:
        with open(output_filename, 'w') as file:
            file.write(f"Word count: {word_count}")
        print(f"Word count written to '{output_filename}' successfully!")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def get_filename(prompt):
    """
    Prompts the user to input a filename.
    Ensures the filename is not empty.
    """
    filename = input(prompt).strip()
    if not filename:
        print("Invalid input! Please provide a valid filename.")
        return None
    return filename

def main():
    print("Welcome to the File Handling Program!")
    while True:
        print("\nChoices:")
        print("1. Count words in a file")
        print("2. Write word count to a new file")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 3.")
            continue

        if choice == 3:
            print("Thank you for using the program. Goodbye!")
            break

        if choice == 1:
            input_filename = get_filename("Enter the name of the file to count words: ")
            if input_filename is None:
                continue

            word_count = count_words_in_file(input_filename)
            if isinstance(word_count, int):
                print(f"The file '{input_filename}' contains {word_count} words.")
            else:
                print(word_count)

        elif choice == 2:
            input_filename = get_filename("Enter the name of the file to count words: ")
            if input_filename is None:
                continue

            word_count = count_words_in_file(input_filename)
            if not isinstance(word_count, int):
                print(word_count)
                continue

            output_filename = get_filename("Enter the name of the output file to save the word count: ")
            if output_filename is None:
                continue

            write_word_count(output_filename, word_count)

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
