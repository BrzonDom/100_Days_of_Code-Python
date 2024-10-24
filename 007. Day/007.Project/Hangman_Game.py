import random
from Hangman_Art import stages, logo

print(logo)
print()

word_list = ["aardvark", "baboon", "camel"]

# word = random.choice(word_list)
word = word_list[1]
word_len = len(word)

display = "_" * word_len

lives = 6

print(f"Word: {word}")
print()

while display != word and lives:

    guess = input("Enter your guess: ").lower()
    print()

    if guess in word:
        for idx, crc in enumerate(word):
            if guess == crc:
                display = display[:idx] + guess + display[idx + 1:]

        print("\tRight guess")
        print(display)
        print()

    else:
        lives -= 1

        print("\tWrong guess")
        print(f"Lives: {lives}")

        print(stages[lives])

if not lives:
    print("You LOSE")

elif display == word:
    print("You WIN")
