import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Word list: {word_list}")
print(f"Chosen word: {chosen_word}")
print()

guess = input("Guess a letter: ").lower()
print()

if guess in chosen_word:
    print("Right")

else:
    print("Wrong")
