"""  Lab 2 -----> Level 3

<<   Variables, Types and Expressions   >>

Create a program that prints a chosen measure in meters and
prints the value in kilometers and in centimeters.

You can assume that the value will not be negative values.
"""

meters = 100

kilometers = meters / 1000
centimeters = meters * 100

print(f"{kilometers} km = {meters} m = {centimeters} cm")