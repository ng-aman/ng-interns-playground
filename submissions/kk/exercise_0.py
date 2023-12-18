# Product details
product_1_name, product_1_price = "Laptop", 1200.0
product_2_name, product_2_price = "Headphones", 50.0
product_3_name, product_3_price = "Mouse", 20.0

# Shopping cart
cart = []

# Add items to the cart
cart.append({"name": product_1_name, "price": product_1_price, "quantity": 2})
cart.append({"name": product_2_name, "price": product_2_price, "quantity": 1})
cart.append({"name": product_3_name, "price": product_3_price, "quantity": 3})

# Calculate total amount
total_ammount = sum(items["price"] * items["quantity"] for items in cart)

# Apply a discount of 10% for a purchase above $100
discount = 0.0
if total_ammount > 100:
    discount = 0.1 * total_ammount

# Calculate the final amount after applying the discount
final_ammount = total_ammount - discount

# Display the receipt
print("------ Shopping Receipt ------")
for items in cart:
    print(f"{items['name']} x {items['quantity']}: ${items['price'] * items['quantity']}")

print(f"\nTotal Amount: ${total_ammount}")
print(f"Discount (10% for purchases above $100): ${discount}")
print(f"Final Amount: ${final_ammount}")
