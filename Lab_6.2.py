"""  Lab 6 -----> Level 2

<<   While Loops   >>

• You are writing a program for a vending machine
• Ask the user to enter the amount of money they currently have and what snack they want to buy.
• The vending machine will keep accepting money and display the current amount it
  has until the total is equal to the snack price or more.
• Then, display “Payment accepted!” and the change (is there is any).

Prices:
Chips .... 15 SEK
Loka .... 10 SEK
Kex .... 5 SEK
"""

product_one   = "chips"
product_two   = "loka"
product_three = "kex"

print(f"""
Menu:
{product_one.capitalize():<5} ...... 15 SEK
{product_two.capitalize():<5} ...... 10 SEK
{product_three.capitalize():<5} ...... 5  SEK
""")

wallet = -1
while wallet != 0:
    try:
        wallet = int(input("Enter the amount of money you have: "))
        if wallet == 0:
            print("Thanks!")
        else:
            product = input("Enter the product you want to buy: ")
            while product.lower() != 'chips' and product.lower() != 'kex' and product.lower() != 'loka':
                    product = input("The chosen product is not in the menu. Try again: ")
            if product.lower() == product_one:
                amount_to_pay = 15
            elif product.lower() == product_two:
                amount_to_pay = 10
            elif product.lower() == product_three:
                amount_to_pay = 5

            while wallet < amount_to_pay:
                wallet += int(input(f"You have {amount_to_pay - wallet} SEK left: "))

            print("Payment accepted!")
            print(f"Your change is {wallet - amount_to_pay} SEK!")
            break

    except Exception:
        print("Invalid input! Enter a number!")