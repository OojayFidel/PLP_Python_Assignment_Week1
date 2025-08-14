# Discount calculation module

# Calculate the discount amount based on the price and discount percentage.
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    if discount_percent >= 20:
        print("High discount applied.")
        return price - discount_amount
    else:
        print("No discount applied.")
        return price
       
# Prompt the user for input
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))     

# Example usage
result = calculate_discount(price, discount_percent)
print(f"Discounted price: {result}")


# This module can be imported in other scripts to use the calculate_discount function.
