# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


def encrypt(org_text, shft):

    pass


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = "Hello World"
shift = 2

print(f"Text: {text}")
print(f"Shift: {shift}")
print()

char_ary = [char for char in text]
print(f"\tCharacter array: {char_ary}")
print()

print(f"\tAlphabet characters: {ord('z') - ord('a')}")
print()
print(f"\tLowercase characters: {ord('a')} - {ord('z')}")
print(f"\t\t'a': {ord('a')}")
print(f"\t\t'z': {ord('z')}")
print()
print(f"\tUppercase characters: {ord('A')} - {ord('Z')}")
print(f"\t\t'A': {ord('A')}")
print(f"\t\t'Z': {ord('Z')}")
