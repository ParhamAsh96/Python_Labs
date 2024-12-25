"""  Lab 8 -----> Level 1

<<   List   >>

Ask the user to type their full name. Then you should find and print the longest part of the user’s name. 
If the user has two or more names with the same number of characters, return the last one.
"""

full_name = input("Enter your full name: ").split()

longest_name_index = 0
for i in range(len(full_name)):
    if len(full_name[longest_name_index]) < len(full_name[i]):
        longest_name_index = i

print(f"Your longest name is {full_name[longest_name_index].capitalize()} ({len(full_name[longest_name_index])} letters).")