# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


def encrypt(org_text, shft):

    pass


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text_org = "fFeEdDcCbBaA"
shift = -6

print(f"Text: {text_org}")
print(f"Shift: {shift}")
print()

text_org_array = [char for char in text_org]

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

for char in text_org_array:
    char_org_val = ord(char)
    print(f"\t\t{char} = chr({char_org_val:3})", end=" : ")

    if ord_a <= char_org_val <= ord_z:
        print("Lowercase letter")

    elif ord_A <= char_org_val <= ord_Z:
        print("Uppercase letter")

    else:
        print("Non-alphabetic character")
print()

print(f"\tShift by: {shift}")
for char in text_org_array:
    char_org_val = ord(char)

    if ord_a <= char_org_val <= ord_z:
        char_new_val = char_org_val + shift

        if char_new_val > 122:
            char_new_val -= 26

        elif char_new_val < 97:
            char_new_val += 26

        print(f"\t\t\'{char}\' -> \'{chr(char_new_val)}\'")

    elif ord_A <= char_org_val <= ord_Z:
        char_new_val = char_org_val + shift

        if char_new_val > 90:
            char_new_val -= 26

        elif char_new_val < 65:
            char_new_val += 26

        print(f"\t\t\'{char}\' -> \'{chr(char_new_val)}\'")

    else:
        print(f"\t\t\'{char}\'")
