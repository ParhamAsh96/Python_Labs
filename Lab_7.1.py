"""  Lab 7 -----> Level 1

<<   Functions and Main   >>

• The personnummer is a social security number in Sweden that carry
the user’s birth year, month and day. The format is:
• YYYYMMDD-XXXX, where XXXX are four control digits.
• Write a program that asks the user for their personnummer and then
prints their age. You can ignore months and days, and calculate the
age based only on the year.
"""

def personnummer(YYYY, MM, DD, XXXX):
    current_year = 2024
    age = current_year - YYYY
    print(f"You are {age} years old!")
    
personnummer(1995, 10, 20, 1234)