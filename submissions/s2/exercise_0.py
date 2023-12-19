# Product details
product1name, product1price = "Laptop", 1200.0
product2name, product2price = "Headphones", 50.0
product3name, product3price = "Mouse", 20.0


# Shopping cart
cart = []

# Add items to the cart
cart.append({"name": product1name, "price": product1price, "quantity": 2})
cart.append({"name": product2name, "price": product2price, "quantity": 1})
cart.append({"name": product3name, "price": product3price, "quantity": 3})

# Calculate total amount
total_amount = sum(item["price"] * item["quantity"] for item in cart)

# Apply a discount of 10% for a purchase above $100
discount = 0.0
if total_amount > 100:
    discount = 0.1 * total_amount

# Calculate the final amount after applying the discount
final_amount = total_amount - discount

# Display the receipt
print("------ Shopping Receipt ------")
for item in cart:
    print(f"{item['name']} x {item['quantity']}: ${item['price'] * item['quantity']}")

print(f"\nTotal Amount: ${total_amount}")
print(f"Discount (10% for purchases above $100): ${discount}")
print(f"Final Amount: ${final_amount}")
