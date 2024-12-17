"""
<<   Conditionals   >>

• Write a program that reads the first and last name of a person. If
the first and last name are equal to one another, then print:
• “Welcome <first_name>”.
• Otherwise, you should print:
• “Welcome <LAST_NAME>, <first_name>.”
"""

first_name = input("Please enter your first name: ")
last_name  = input("Please enter your last name: ")

if first_name == last_name:
    print(f"Welcome {first_name.capitalize()}.")
else:
    print(f"Welcome {last_name.upper()}, {first_name.capitalize()}.")