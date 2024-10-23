import random

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

print(f"Word: {word}")
print()

guess = input("Enter your guess: ").lower()
print()

if guess in word:
    print("Right")

else:
    print("Wrong")
