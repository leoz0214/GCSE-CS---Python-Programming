# Task 6.1d - Code maker and breaker (lite version)


def letter_to_number():
    letter = input("Enter a letter (a-z): ")
    return f"{letter} = {letters.index(letter)+1}" if letter in letters else "Invalid letter, try again"


def number_to_letter():
    try:
        number = int(input("Enter a number (1-26): "))
    except ValueError:
        return "Enter an integer!"
    else:
        return f"{number} = {letters[number-1]}" if 0 < number <= 26 else "Invalid number, try again"


def main():
    while True:
        selection = input("""\nCode Maker (and Breaker)\n1 - Encode a letter\n2 - Decode a letter\n9 - Exit\nEnter an option: """).strip()
        if selection == "1":
            print(letter_to_number())
        elif selection == "2":
            print(number_to_letter())
        elif selection == "9":
            return "Goodbye!"
        else:
            print("Error, invalid input. Please retry")


if __name__ == "__main__":
    letters = tuple("abcdefghijklmnopqrstuvwxyz")
    print(main())

