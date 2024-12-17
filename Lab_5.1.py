"""
<<   For Loops   >>

• Ask the user to enter a number
• Create a multiplication table (from 1 to 10) of the number.

• For example, for number 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
"""

number = int(input("Please enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")