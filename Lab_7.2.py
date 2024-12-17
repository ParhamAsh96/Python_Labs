"""  Lab 7 -----> Level 2

<<   Functions and Main   >>

• Create a menu with tasks that reads and parses a personnummer (social security number).
• Calculate the person’s age, and print their gender.
• Begin by reading a personnummer: YYYYMMDD-XXXX
• You can assume that the user will type all characters of the personnumer as the format above.
• Gender is defined by the the second-last digit: YYYYMMDD-XXGX
• The digit is odd for men, even for women.

• The Menu should be:
Welcome to the personnummer checker:
1. Read new personnummer:
2. Check the age
3. Check gender
4. Exit the program
Type your option:

• Summary of Tasks:
• Start reading personnummer
• Use the birth year to calculate age.
• Use the last to second digit to calculate gender.
"""

def personnummer_checker():
    invalid_input = False
    while not invalid_input:
        try:
            personnummer = input("Enter your personal number with the format YYYYMMDDXXXX: ")
            YYYY = int(personnummer[0:4])
            MM   = int(personnummer[4:6])
            DD   = int(personnummer[6:8])
            XXXX = int(personnummer[8:13])

            return YYYY, MM, DD, XXXX
        
        except ValueError:
            print("Invalid Input! Enter only numbers!")


def age_checker(YYYY):
    current_year = 2024
    age = current_year - YYYY

    print(f"You are {age} years old.")
    return age


def gender(YYYY, MM, DD, XXXX):

    string_XXXX = str(XXXX)
    XXGX = int(string_XXXX[2])

    if XXGX % 2 == 0:
        print("You are a woman!")
    elif XXGX % 2 == 1:
        print("You are a man!")


def menu(option, YYYY, MM, DD, XXXX):
    match option:
        case 1:
            YYYY, MM, DD, XXXX = personnummer_checker()
            return YYYY, MM, DD, XXXX
        case 2:
            age_checker(YYYY)
        case 3:
            gender(YYYY, MM, DD, XXXX)
        case 4:
            print("Goodbye!")
            exit()
        case _:
            print("Invalid Input!")


def menu_display():
    print(f"""
    ........................................
    ----------------------------------------
    |                 Menu                 |
    ----------------------------------------
    |       Please choose one option       |
    ----------------------------------------
    |  (1)  Enter a new personnummer       |
    ----------------------------------------
    |  (2)       Check your age            |
    ----------------------------------------
    |  (3)     Check your gender           |
    ----------------------------------------
    |  (4)            Exit                 |
    ----------------------------------------
    ----------------------------------------
            """)
    

# Main Program
def main():

    print(f"""
    ........................................
    ----------------------------------------
    | Welcome to the personnummer checker! |
    ----------------------------------------
          """)
          
    YYYY, MM, DD, XXXX = personnummer_checker()
    menu_display()

    invalid_input = False
    while not invalid_input:
        try:
            while True:
                option = int(input("Choose an option (1-4): "))
                result = menu(option, YYYY, MM, DD, XXXX)
                if result:
                    YYYY, MM, DD, XXXX = result
        except ValueError:
            print("Invalid input!")


if __name__ == "__main__":
    main()