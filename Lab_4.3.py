"""
<<   Conditionals   >>

• Combine your Month and Age to find out your guardian animal.
• Read the month in which the user was born (1, 2, 3, ..., 12).
• Read the age of the user.
• Use the information to print what is their:
• Element: every third month has a different element.
• Animal: every 5th year (starting at 0) has a different animal.
• Print: “You are a <element> <animal>”

January, May, September: Earth
February, June, October: Wind
March, July, November: Water
April, August, December: Fire
0 year(s) old = Shark
1 year(s) old = Scorpion
2 year(s) old = Jaguar
3 year(s) old = Crane
4 year(s) old = Dragon
5 = Shark
6 = Scorpion
7 = Jaguar
8 = Crane
9 = Dragon
15 = Shark
16 = Scorpion
17 = Jaguar
18 = Crane
19 = Dragon
20 = Shark
21 = Scorpion
22 = Jaguar
23 = Crane
24 = Dragon
Continue for all years using the pattern above.
"""

month = int(input("Please enter your birth month: "))
age = int(input("How old are you? "))

element = ""
animal  = ""

# Condition
if month == 1 or month == 5 or month == 9:
    element = "Earth"

elif month == 2 or month == 6 or month == 10:
    element = "Wind"

elif month == 3 or month == 7 or month == 11:
    element = "Water"

elif month == 4 or month == 8 or month == 12:
    element = "Fire"

else:
    print("Invalid input!")


if age % 5 == 0:
    animal = "Shark"

elif age % 5 == 1:
    animal = "Scorpion"

elif age % 5 == 2:
    animal = "Jaguar"

elif age % 5 == 3:
    animal = "Crane"

elif age % 5 == 4:
    animal = "Dragon"

else:
    print("Invalid input!")


# Result
print(f"You are a {element} {animal}.")