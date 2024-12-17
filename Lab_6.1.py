"""
<<   While Loops   >>

• Write a program that helps employees manage their working hours.
• Repeatedly asks the user to enter the number of hours they worked so far.
• The program should keep a running until the total hours reach 8 or more
• Then, the program should display a message saying, "You have completed your shift!" and exit.
"""

working_hours = int(input("Enter how many hours you've worked: "))

while working_hours <= 8:
    working_hours_1 = int(input("Enter how many hours you've worked: "))
    working_hours += working_hours_1

print(f"\nYou've worked {working_hours} hours and completed your shift!")