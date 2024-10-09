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
    print(f"\t{idx}.: {wrd[idx]} | {wrd[-(idx+1)]}")
print()

print("124")
print("876")
print("124" + "876")
print()

print(124)
print(876)
print(124 + 876)


"""__Output__"""
"""
Word: Hello
	Word length:5

	0.: H | o
	1.: e | l
	2.: l | l
	3.: l | e
	4.: o | H
	
124
876
124876

124
876
1000

Process finished with exit code 0
"""
