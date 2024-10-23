import random

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
word_len = len(word)

placeholder = "_" * word_len

print(f"Word: {word}")
print()

guess = input("Enter your guess: ").lower()
print()

if guess in word:
    print("Right")

else:
    print("Wrong")
