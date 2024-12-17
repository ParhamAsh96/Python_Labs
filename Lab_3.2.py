"""
<<   User Input and Formatted Strings   >>

Ask the user to type the name of 5 products and their respective price.
• Decide on how to split your prompts to the user, and write in a comment a reflection justifying your choice of prompt.
• Print the list of products using the given template (next slide).
• Bonus: Print also the average price of all products.
• The average is the sum of all products divided by the number of products.
• Don’t use the rounded value

• 20 characters limit on product name.
• If more than 20, cut at 20.
• If less than 20, pad left with empty space
• Average in example: ca 5306.04

• 2 decimal places.
• Ignore rounding differences.
• If less than 4 whole digits, pad with empty space.
• For more than 4 whole digits, ignore alignment.

Chocolate, 5.123
Chips (Hot Cheese Nachos), 25.1234
Tea, 350.2
Sony "Playstation 5", 7500.0
Samsung OLED TV, 18999.9999999
"""

products = {}

for i in range(0, 5):
    product = input(f"Enter your {i + 1}'s product: ")
    price = float(input(f"What is the price of {i + 1}'s product? "))

    product = product.capitalize()

    products[product] = price

print("\nGroceries: ")
for product, price in products.items():
    print(f"{product[:20]:>20}:............ $ {price:>8.2f}")