import random

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

print(f"Word: {word}")
