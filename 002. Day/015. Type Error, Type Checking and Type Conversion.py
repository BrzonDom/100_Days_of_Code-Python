"""
Type Error, Checking and Conversion

    TypeError
        These errors occur when you are using the wrong data type. e.g. len(12345)
        Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you
        give it a number (Integer).

        PAUSE 1. Fix the len() function so it has no more warnings or errors.

    Type Checking
        You can check the data type of any value or variable in python using the type() function.

        print(type("abc")) #will give you <class 'str'>

        PAUSE 2. Write out 4 type checks to print all 4 data types

        Using the type() and print() functions to print out 4 lines into the output area so we get the full
        collection of data types that we learnt about. <class 'str'> <class 'int'> <class 'float'> and <class 'bool'>

    Type Conversion
        You can convert data into different data types using special functions. e.g.

            float()
            int()
            str()

        PAUSE 3. Make this line of code run without errors

        print("Number of letters in your name: " + len(input("Enter your name")))

"""


"""__Code__"""

print("Data types: \n")

String = "String"
print(f"\t{String}")
print(f"\t\t{type(String)}")

Integer = 123
print(f"\t{Integer}")
print(f"\t\t{type(Integer)}")

Float = 3.141
print(f"\t{Float}")
print(f"\t\t{type(Float)}")

Boolean = True
print(f"\t{Boolean}")
print(f"\t\t{type(Boolean)}")
print()

print(str(1))
print(int("1"))
print(float(1))
print(bool(1))


"""__Output__"""
"""
Data types: 

	String
		<class 'str'>
	123
		<class 'int'>
	3.141
		<class 'float'>
	True
		<class 'bool'>

1
1
1.0
True

Process finished with exit code 0
"""
