"""
Declare two variables to represent a product price and a discount percentage.
Declare a variable with the product name.
Calculate the price of the product, after applying the discount
Print the product along with its final price.
"""

product = "Playstation 5"
price = 10995

discount = 0.20
discount_percentage = int(discount * 100)

discounted_price = price - (price * discount)

print(f"{product} costs {discounted_price} SEK with a {discount_percentage}% discount.")