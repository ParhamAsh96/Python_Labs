"""  Lab 7 -----> Level 3

<<   Functions and Main   >>

• Case 1: Make a robust program where users can type:
• 19800101-1234 or 800101-1234
• To distinguish between years, when a person turns 100, the ‘–’ is replaced with a ‘+’ sign:
• 230202-1234 : 1 year old (born in 2023)
• 230202+1234: 101 years old (born in 1923)

• Case 2: If the user types more or less characters, print the message:
• “Invalid Personnumer. Type YYYYMMDD-XXXX or YYMMDD-XXXX”
• Keep reading the personnumer until the user typed a valid input.
"""

def personnummer_reader():
    invalid_input = False
    while not invalid_input:
        try:
            personnummer = input("Enter your personnummer: ")

            YYYY = int(personnummer[0:4])
            MM   = int(personnummer[4:6])
            DD   = int(personnummer[6:8])
            XXXX = int(personnummer[8:12])

            print(YYYY)
            print(MM)
            print(DD)
            print(XXXX)
            invalid_input = True

            if len(personnummer) < 10 and len(personnummer) > 12:
                print("The format needs to be YYYYMMDD-XXXX or YYMMDD-XXXX: ")
        except ValueError:
            print("Invalid input! Enter only numbers!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
personnummer_reader()

    
    #return YYYY, MM, DD, XXXX

"""
def calculation(YYYY, MM, DD, XXXX):
    print("test")
"""

"""def main():
    YYYY, MM, DD, XXXX = input()
    input()"""


"""if __name__ == "__main__":
    main()"""