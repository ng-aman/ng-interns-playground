# Product details
product1_name, product1_price = "Shirt", 1200.0
product2_name, product2_price = "Kurtis", 50.0
product3_name, product3_price = "Earings", 20.0

# Shopping cart is also called as buggy in USA
buggy = []

# Add items to the cart
buggy.append({"name": product1_name, "price": product1_price, "quantity": 2})
buggy.append({"name": product2_name, "price": product2_price, "quantity": 1})
buggy.append({"name": product3_name, "price": product3_price, "quantity": 3})

# Calculate total amount
total_price = sum(item["price"] * item["quantity"] for item in buggy)

# Apply a discount of 10% for a purchase above $100
discount = 0.0
if total_price > 100:
    discount = 0.1 * total_price

# Calculate the final amount after applying the discount
grand_total = total_price - discount

# Display the receipt
print("------ Shopping Receipt ------")
for item in buggy:
    print(f"{item['name']} x {item['quantity']}: ${item['price'] * item['quantity']}")

print(f"\nTotal Amount: ${total_price}")
print(f"Discount (10% for purchases above $100): ${discount}")
print(f"Final Amount: ${grand_total}")
