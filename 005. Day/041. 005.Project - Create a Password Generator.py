"""
  5. Project - Create a Password Generator

    The program will ask:

        How many letters would you like in your password?
        How many symbols would you like?
        How many numbers would you like?

    The objective is to take the inputs from the user to these questions and then generate a random password. Use your
    knowledge about Python lists and loops to complete the challenge.

    Demo:
        https://appbrewery.github.io/python-day5-demo/

    Easy Version:

        Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

        4 letters 2 symbols and 3 numbers then the password might look like this:

        fgdx$*924

        You can see that all the letters are together. All the symbols are together and all the numbers follow each
        other as well. Try to solve this problem first.

        Hint 1:
            Remember you can use the random.choice() function to get a random item from a List! But you need to import
            the random module first.

    Hard Version:

        When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of
        this project the final password does not follow a pattern. So the example above might look like this:

        x$d24g*f9

        And every time you generate a password, the positions of the symbols, numbers, and letters are different. This
        will make the password more difficult for hackers to crack.

        The essential skill of a good programmer is using Google to find what you need. Your brain is for thinking,
        not memorising functions! You will need to Google to solve this project on the hard level. If you get stuck,
        check the hint below for what to Google.

        Hint 2:
            Try googling: "How to shuffle items in a List in Python"

"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_letters = 6
print("How many letters would you like in your password?")
print(nr_letters)
nr_symbols = 2
print("How many symbols would you like?")
print(nr_symbols)
nr_numbers = 4
print("How many numbers would you like?")
print(nr_numbers)
print()

print(f"Letters: {nr_letters}")
print(f"Symbols: {nr_symbols}")
print(f"Numbers: {nr_numbers}")

ps_letters = ""
ps_symbols = ""
ps_numbers = ""

for crc in range(nr_letters):
    rn_letter = random.choice(letters)

for crc in range(nr_symbols):
    rn_symbol = random.choice(symbols)

for crc in range(nr_numbers):
    rn_number = random.choice(numbers)
