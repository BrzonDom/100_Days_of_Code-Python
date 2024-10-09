"""
Data Types

    Learn about the primitive data types in Python.

        1. Strings
        2. Integers
        3. Floats
        4. Booleans

"""


"""__Code__"""

wrd = "Hello"
ln_wrd = len(wrd)

print(f"Word: {wrd}")
print(f"\tWord length:{ln_wrd}")
print()

for idx in range(ln_wrd):
    print(f"\t{idx}.: {wrd[idx]}")


"""__Output__"""
"""
Word: Hello
	Word length:5

	0.: H
	1.: e
	2.: l
	3.: l
	4.: o

Process finished with exit code 0
"""
