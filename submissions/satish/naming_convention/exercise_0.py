# Product details
product_name_1, product_price_1 = "Laptop", 1200.0
product_name_2, product_price_2 = "Headphones", 50.0
product_name_3, product_price_3 = "Mouse", 20.0

# Shopping cart
cart = []

# Add items to the cart
cart.append({"name": product_name_1, "price": product_price_1, "quantity": 2})
cart.append({"name": product_name_2, "price": product_price_2, "quantity": 1})
cart.append({"name": product_name_3, "price": product_price_3, "quantity": 3})

# Calculate total amount
total_amount = sum(items["price"] * items["quantity"] for items in cart)

# Apply a discount of 10% for a purchase above $100
discount = 0.0
if total_amount > 100:
    discount = 0.1 * total_amount

# Calculate the final amount after applying the discount
final_amount = total_amount - discount

# Display the receipt
print("------ Shopping Receipt ------")
for items in cart:
    print(f"{items['name']} x {items['quantity']}: ${items['price'] * items['quantity']}")

print(f"\nTotal Amount: ${total_amount}")
print(f"Discount (10% for purchases above $100): ${discount}")
print(f"Final Amount: ${final_amount}")
