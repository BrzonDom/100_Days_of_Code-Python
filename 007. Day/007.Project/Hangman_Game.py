import random

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
word_len = len(word)

display = "_" * word_len

print(f"Word: {word}")
print()

guess = input("Enter your guess: ").lower()
print()

if guess in word:
    for crc in word:
        if guess == crc:
            print("Right")

else:
    print("Wrong")
