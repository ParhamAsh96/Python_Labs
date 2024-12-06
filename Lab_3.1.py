"""
Ask the user to type the name of 5 of their favourite artists.
• Remember to distinguish between first name and last name when prompting.
• Print the First and Last name of your chosen artists using the example below.
• Last name must be completely uppercase
• Padded left or cut after 8.
• Last name must fit 8 characters

   CAREY, Mariah
 HOUSTON, Whitney
        , Cher
        , Beyonce
    GAGA, Lady
NEWTON-J, Olivia
WINEHOUS, Amy
"""

name_list = []

for i in range(0, 7):
    first_name = input(f"Please enter the first name of your favorite artist {i + 1}: ")
    last_name  = input(f"Please enter the last name of your favorite artist {i + 1}: ")

    name_list.append(f"{last_name.upper()[:8]:>8}, {first_name.capitalize()}")

print("\nHere is the list of your favorite artists: \n")

for artist in name_list:
    print(artist)

