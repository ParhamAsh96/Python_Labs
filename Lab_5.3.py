"""
<<   For Loops   >>

• Ask the user to type the name of 5 products and their respective price.
• Decide on how to split your prompts to the user, and write in a comment a
reflection justifying your choice of prompt.
• Print the list of products using the given template (next slide).
• Print also the average price of all products.
• The average is the sum of all products divided by the number of products.

• 20 characters limit on product name.
• If more than 20, cut at 20.
• If less than 20, pad left with empty space
• 2 decimal digits, with a comma.
• Ignore rounding differences.
• If less than 4 whole digits, pad with empty space.
• For more than 4 whole digits, ignore alignment.

Chocolate, 5.123455
Chips (Hot Cheese Nachos), 25.123455
Tea, 350.2
Sony "Playstation 5", 7500.0
Samsung OLED TV, 18999.9999999
"""

products = []
prices = []

for i in range(1, 6):
    product = input(f"\nEnter the {i}'s product: ")
    products.append(product)
    price = round(float(input(f"Enter the price of the {i}'s product: ")), 2)
    prices.append(price)

print("Groceries:")
for product, price in zip(products, prices):
    print(f"{product[:20]:>20}............$ {price:<4}")