"""  Lab 4 -----> Level 2 

<<   Conditionals   >>

• Write a program that reads the name of a person, three times.
• If the same name is entered consecutively, then print the message:
• “Hey <name>, you already entered your name.”
• Otherwise, print the message:
• “Welcome to our guests: <name1>, <name2>, <name3>.”

Input: Sam Sam Jane Output: Hey Sam, you already entered your name.
Input: Sam Jane Sam Output: Welcome to our guests: Sam Jane Sam
Input: Sam Jane Jane Output: Hey Jane, you already entered your name.
Input: Sam Jane John Output: Welcome to our guests: Sam Jane John
"""

name_one   = input("Please add your name to our guest list: ")
name_two   = input("Please add your name to our guest list: ")
name_three = input("Please add your name to our guest list: ")

if name_one == name_two or name_two == name_three:
    print(f"Hey {name_two.capitalize()}, you already entered your name.")
else:
    print(f"Welcome to our guests: {name_one.capitalize()}, {name_two.capitalize()}, {name_three.capitalize()}.")
