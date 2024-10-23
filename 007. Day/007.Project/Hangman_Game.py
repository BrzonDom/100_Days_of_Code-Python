import random

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
