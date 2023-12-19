
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
total_price = sum(product["price"] * product["quantity"] for product in cart)

# Apply a discount of 10% for a purchase above $100
dicount = 0.0
if total_price > 100:
    discount = 0.1 * total_price

# Calculate the final amount after applying the discount
final_amount = total_price - discount

# # Display the receipt
print("------ Shopping Receipt ------")
for product in cart:
    print(f"{product['name']} x {product['quantity']}: ${product['price'] * product['quantity']}")

print(f"\nTotal Amount: ${total_price}")

# Check if a discount was applied before printing
if discount > 0:
    print(f"Discount (10% for purchases above $100): ${discount}")
    print(f"Final Amount: ${final_amount}")
else:
    print("No discount applied.")

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
total_price = sum(product["price"] * product["quantity"] for product in cart)

# Apply a discount of 10% for a purchase above $100
dicount = 0.0
if total_price > 100:
    discount = 0.1 * total_price

# Calculate the final amount after applying the discount
final_amount = total_price - discount

# # Display the receipt
print("------ Shopping Receipt ------")
for product in cart:
    print(f"{product['name']} x {product['quantity']}: ${product['price'] * product['quantity']}")

print(f"\nTotal Amount: ${total_price}")

# Check if a discount was applied before printing
if discount > 0:
    print(f"Discount (10% for purchases above $100): ${discount}")
    print(f"Final Amount: ${final_amount}")
else:
    print("No discount applied.")

    print(f"Final Amount: ${final_amount}")