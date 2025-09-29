"""  Lab 9 -----> Level 1

<<   Tuple   >>

Level 1:
You are hired to create a game where heroes and villains will battle each other. 
Each hero and villain has: a name, and a power. The game will use an interactive menu.
When summoning a hero or villain, ask the user for their name and power.
Store their name and power in a tuple.


Template:
Part 1: Menu
    Welcome to the battleground!
    1. End game
    2. Summon Hero
    3. Summon Villain
    4. Print Teams

Part 2: Output
    Heroes:
    - Storm: 100 power
    - Ironman: 60 power 
    - Dr. Strange: 80 power

    Villains:
    - Dr. Doom: 90 power
    - Venom: 60 power
    - Magneto: 90 power
    - Mystique: 65 power
"""


def menu():
    team_heros = []
    team_villain = []
    option = 0

    while option != 1:
        print("""
Welcome to the battleground!
1. End game
2. Summon Hero
3. Summon Villain
4. Print Teams
          """)
        try:
            option = int(input("\nPlease choose an option: "))

            if option == 1:
                print("Goodbye!")

            elif option == 2:
                hero = read__hero()
                team_heros.append(hero)
                
            elif option == 3:
                villain = read__villain()
                team_villain.append(villain)
                
            elif option == 4:
                print("\nHeroes: ")
                print_heroes(team_heros)

                print("\nVillains: ")
                print_villains(team_villain)
            
            else:
                print("Please choose a number between 1-4!")

        except Exception:
            print("Please choose a number between 1-4!")
        

def read__hero():
    hero = input("Enter the Hero: ").capitalize()

    is_finished = False
    while not is_finished:
        try:
            h_power = int(input("Enter the hero's power: "))
            is_finished = True
        
        except ValueError:
            print("\nPlease enter a number!\n")

    return hero, h_power


def read__villain():
    villain = input("Enter the Villain: ").capitalize()

    is_finished = False
    while not is_finished:
        try:
            v_power = int(input("Enter the villain's power: "))
            is_finished = True
        
        except ValueError:
            print("\nPlease enter a number!\n")

    return villain, v_power


def print_heroes(team_heros):
    for hero in team_heros:
        print(f"- {hero[0]}: {hero[1]} power")


def print_villains(team_villain):
    for villains in team_villain:
        print(f"- {villains[0]}: {villains[1]} power")


def main():
    menu()


if __name__ == "__main__":
    main()