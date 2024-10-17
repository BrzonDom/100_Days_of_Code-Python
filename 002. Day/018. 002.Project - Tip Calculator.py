"""
  2. Project - Tip Calculator

    We're going to build a tip calculator.

    If the bill was $150.00, split between 5 people, with 12% tip.

    Each person should pay:

        (150.00 / 5) * 1.12 = 33.6

    After formatting the result to 2 decimal places = 33.60

    Demo:
        https://appbrewery.github.io/python-day2-demo/

    Very Optional Reading: Floating Point Arithmetic
        https://docs.python.org/3/tutorial/floatingpoint.html

"""


print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# bill = 150
# tip = 12
# people = 5
#
# print("What was the total bill? $")
# print(bill)
# print("What percentage tip would you like to give? 10 12 15 ")
# print(tip)
# print("How many people to split the bill? ")
# print(people)
print()

total = bill * (1 + tip * 0.01)
print(f"Total: {total:.2f}")
part = total / people
part = round(part, 2)
print(f"Part: {part:.2f}")
