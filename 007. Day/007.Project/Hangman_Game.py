import random

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

word_list = ["aardvark", "baboon", "camel"]

# word = random.choice(word_list)
word = word_list[1]
word_len = len(word)

display = "_" * word_len

print(f"Word: {word}")
print()

while display != word:

    guess = input("Enter your guess: ").lower()
    print()

    if guess in word:
        for idx, crc in enumerate(word):
            if guess == crc:
                print(f"{idx+1}. Right")

                print(display[:idx] + guess + display[idx + 1:])
                display = display[:idx] + guess + display[idx + 1:]

    else:
        print("Wrong")
