import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

word_len = len(chosen_word)
placeholder = "_" * word_len
print(placeholder)
print()

guess = input("Guess a letter: ").lower()
print()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter

    else:
        display += '_'

print(display)
