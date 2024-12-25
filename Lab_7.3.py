"""  Lab 7 -----> Level 3

<<   Functions and Main   >>

• Case 1: Make a robust program where users can type: 19800101-1234 or 800101-1234
• To distinguish between years, when a person turns 100, the ‘–’ is replaced with a ‘+’ sign:
• 230202-1234 : 1 year old (born in 2023)
• 230202+1234: 101 years old (born in 1923)

• Case 2: If the user types more or less characters, print the message:
• “Invalid Personnumer. Type YYYYMMDD-XXXX or YYMMDD-XXXX”
• Keep reading the personnumer until the user typed a valid input.
"""

current_year = 2025

def personnummer_reader():

    invalid_input = False
    while not invalid_input:
        try:
            personnummer = input("Enter your personnummer: ")

            if len(personnummer) < 10 or len(personnummer) > 12 or len(personnummer) == 11:
                print("The format needs to be YYYYMMDD-XXXX or YYMMDD-XXXX: ")
            else:
                if len(personnummer) == 10:
                    YYYY = int(personnummer[0:2])
                    MM   = int(personnummer[2:4])
                    DD   = int(personnummer[4:6])
                    XXXX = int(personnummer[6:10])

                    old_century = 1900
                    new_century = 2000

                    if YYYY >= 0 or YYYY < 25:
                        YYYY += new_century
                        user_age = current_year - YYYY

                        if user_age < 100:
                            print(f"You are {user_age} years old!")
                            print(f"{YYYY}{MM}{DD}-{XXXX}")
                            invalid_input = True
                        
                        elif user_age >= 100:
                            print(f"You are {user_age} years old!")
                            print(f"{YYYY}{MM}{DD}+{XXXX}")
                            invalid_input = True
                        
                    else:
                        YYYY += old_century
                        user_age = current_year - YYYY
                    
                        if user_age < 100:
                            print(f"You are {user_age} years old!")
                            print(f"{YYYY}{MM}{DD}-{XXXX}")
                            invalid_input = True
                        
                        elif user_age >= 100:
                            print(f"You are {user_age} years old!")
                            print(f"{YYYY}{MM}{DD}+{XXXX}")
                            invalid_input = True

                elif len(personnummer) == 12:
                    YYYY = int(personnummer[0:4])
                    MM   = int(personnummer[4:6])
                    DD   = int(personnummer[6:8])
                    XXXX = int(personnummer[8:12])

                    user_age = current_year - YYYY

                    if user_age < 100:
                        print(f"You are {user_age} years old!")
                        print(f"{YYYY}{MM}{DD}-{XXXX}")
                        invalid_input = True
                    
                    elif user_age >= 100:
                        print(f"You are {user_age} years old!")
                        print(f"{YYYY}{MM}{DD}+{XXXX}")
                        invalid_input = True

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
personnummer_reader()