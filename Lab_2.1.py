"""
You work in a dog shelter that has 81 dogs. 22 of
these dogs are puppies. Write a program that
prints the proportion of puppies in the shelter in
percentage. Round to 1 decimal.
• Tip: Use the round(value, decimals) command.
• How many variables do you have in your program?
What are their types?
"""

dogs = 81
puppies = 22

calculation = round((puppies/dogs)*100, 1)

print(calculation)