"""
<<   While Loops   >>

• You are writing a program for Star Park, a company that manages parking lots.
• Register a parking location and capacity (how many cars it can take).
• Continuously ask whether a car is "entering" or "leaving" the parking lot, and display the current number
of cars in the lot after each time a car enters or leaves.
• Only allow cars to enter if the parking lot has a space for them.
• If a car is leaving and the parking lot is empty, just say: ”Cannot leave if parking lot empty!”
• As a programmer, think about what condition to have to terminate this program, then apply it to your
code.
"""

parking_location = input("Register your parking location: ")

valid_input = False
while not valid_input:
    try:
        total_lots = int(input("How many lots does the parking have: "))
        while total_lots < 1:
            total_lots = int(input("The amount of lots can't be 0 or negative. Try again: "))
        valid_input = True
    except ValueError:
        print("Invalid input!")
        print("Please enter number!")

total_cars = 0

valid_input = False
while not valid_input and total_lots != 0:
    try:
        car_registering = input("Is the car entering or leaving? ").strip().lower()
        if car_registering not in ['entering', 'leaving', 'exit']:
            raise ValueError("Invalid input! Please enter 'entering' or 'leaving' or 'exit' if you wish to exit the program.")
        
        if car_registering == 'entering':
            total_cars += 1

            if total_cars > total_lots:
                print("There is no free lot right now. Come back later!")
                total_cars -= 1
                
            elif total_cars <= total_lots:
                print(f"Parked cars: {total_cars}")    

        elif car_registering == 'leaving':
            total_cars -= 1

            if total_cars < 0:
                print("Cannot leave if parking lot empty!")
                total_cars += 1
            else:
                print(f"Parked cars: {total_cars}")
        
        elif car_registering == 'exit':
            print("You exited the program. Bye!")
            valid_input = True

    except ValueError as e:
        print(e)