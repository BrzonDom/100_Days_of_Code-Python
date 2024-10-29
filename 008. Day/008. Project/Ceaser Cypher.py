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
print()

for char in text_array:
    char_val = ord(char)
    print(f"\t\t{char} = chr({char_val:3})", end=" : ")

    if ord_a <= char_val <= ord_z:
        print("Lowercase letter")

    elif ord_A <= char_val <= ord_Z:
        print("Uppercase letter")

    else:
        print("Non-alphabetic character")
print()

print(f"\tShift by: {shift}")
for char in text_array:
    print(f"\t\t{char} -> {chr(ord(char) + shift)}")
