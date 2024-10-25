import random
from Hangman_Art import stages, logo
from Hangman_Words import word_list

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.


print(logo)
print()

# word = random.choice(word_list)
word = word_list[16]
word_len = len(word)

display = "_" * word_len

lives = lives_max = 6

print(f"Word: {word}")
print()

while display != word and lives:

    print(f"****************************{lives}/{lives_max} LIVES LEFT****************************")
    print()

    guess = input("Enter your guess: ").lower()
    print()

    if guess in word:
        for idx, crc in enumerate(word):
            if guess == crc:
                display = display[:idx] + guess + display[idx + 1:]

        print(f"\tRight guess, the letter \'{guess}\' is in the word {word.count(guess)} times")
        print()
        print(display)
        print()

    else:
        lives -= 1

        print(f"\tWrong guess, the letter \'{guess}\' is not in the word")

        print(stages[lives])

if not lives:
    print("***********************YOU LOSE**********************")
    print()
    print(f"The word: {word}")

elif display == word:
    print("***********************YOU LOSE**********************")
