import random
from Hangman_Art import stages, logo

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

# TODO-2: - Update the code below to use the stages List from the file hangman_art.py

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#  e.g. You guessed d, that's not in the word. You lose a life.

# TODO-6: - Update the code below to tell the user how many lives they have left.

# TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.

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
