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

st_nm1 = "124"
st_nm2 = "876"

print("String numbers::")
print(f"\t1.Num.: {st_nm1}")
print(f"\t2.Num.: {st_nm2}")
print(f"\tSum:    {st_nm1} + {st_nm2} = {st_nm1 + st_nm2}")
print()

it_nm1 = 124
it_nm2 = 876

print("Integer numbers:")
print(f"\t1.Num.: {it_nm1}")
print(f"\t2.Num.: {it_nm2}")
print(f"\tSum:    {it_nm1} + {it_nm2} = {it_nm1 + it_nm2}")
print()

print("Large integer numbers:")
print(f"\t123_456_789 = {123_456_789}")
print()

print("Float numbers:")
print(f"\t{3.1415}")
print(f"\t{1.0}")
print(f"\t{1.}")
print(f"\t{-1.0}")
print(f"\t{0.}")
print()

print(True)
print(False)


"""__Output__"""
"""
Word: Hello
	Word length:5

	0.: H | o
	1.: e | l
	2.: l | l
	3.: l | e
	4.: o | H
	
String numbers::
	1.Num.: 124
	2.Num.: 876
	Sum:    124 + 876 = 124876

Integer numbers:
	1.Num.: 124
	2.Num.: 876
	Sum:    124 + 876 = 1000

Large integer numbers:
	123_456_789 = 123456789

Float numbers:
	3.1415
	1.0
	1.0
	-1.0
	0.0

True
False

Process finished with exit code 0
"""
