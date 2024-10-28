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

text_array = [char for char in text]
print(f"\tCharacter array: {text_array}")
print()

ord_a = ord('a')
ord_z = ord('z')
ord_A = ord('A')
ord_Z = ord('Z')

print(f"\tAlphabet characters: {ord_z - ord_a}")
print()
print(f"\tLowercase characters: {ord_a} - {ord_z}")
print(f"\t\t'a': {ord_a}")
print(f"\t\t'z': {ord_z}")
print()
print(f"\tUppercase characters: {ord_A} - {ord_Z}")
print(f"\t\t'A': {ord_A}")
print(f"\t\t'Z': {ord_Z}")

for char in text_array:
    char_val = ord(char)
    print(char, ':', char_val)
