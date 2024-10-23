import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Word list: {word_list}")
print(f"Chosen word: {chosen_word}")
print()

guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
