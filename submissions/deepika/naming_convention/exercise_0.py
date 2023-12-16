# Product details
product1_name, product1_price = "Shirt", 1200.0
product2_name, product2_price = "Kurtis", 50.0
product3_name, product3_price = "Earings", 20.0

# Shopping cart is also called as buggy in USA
Buggy = []

# Add items to the cart
Buggy.append({"name": product1_name, "price": product1_price, "quantity": 2})
Buggy.append({"name": product2_name, "price": product2_price, "quantity": 1})
Buggy.append({"name": product3_name, "price": product3_price, "quantity": 3})

# Calculate total amount
Total_Price = sum(item["price"] * item["quantity"] for item in Buggy)

# Apply a discount of 10% for a purchase above $100
discount = 0.0
if Total_Price > 100:
    discount = 0.1 * Total_Price

# Calculate the final amount after applying the discount
Grand_Total = Total_Price - discount

# Display the receipt
print("------ Shopping Receipt ------")
for item in Buggy:
    print(f"{item['name']} x {item['quantity']}: ${item['price'] * item['quantity']}")

print(f"\nTotal Amount: ${Total_Price}")
print(f"Discount (10% for purchases above $100): ${discount}")
print(f"Final Amount: ${Grand_Total}")
