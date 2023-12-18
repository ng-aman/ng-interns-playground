class Goods:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Order:
    def __init__(self):
        self.products = []

    def add_item(self, item, quantity):
        self.products.append({"item": item, "quantity": quantity})

    def total(self):
        total = 0
        for item in self.products:
            total += item["item"].cost * item["quantity"]
        return total


class BillGenerator:
    def __init__(self, order):
        self.order = order

    def generate_bill(self):
        total_amount = self.order.total()
        service_tax = 0.05 * total_amount  # Assuming 5% service tax
        gst = 0.18 * total_amount  # Assuming 18% GST

        bill_price = total_amount + service_tax + gst

        # Display the bill
        print("------ Bill ------")
        for item in self.order.products:
            print(f"{item['item'].name} x {item['quantity']}: {item['item'].cost * item['quantity']}")

        print(f"\nTotal Amount: {total_amount}")
        print(f"Service Tax (5%): {service_tax}")
        print(f"GST (18%): {gst}")
        print(f"Final Amount: {bill_price}")


# Example usage:
item1 = Goods("item1", 10.0)
item2 = Goods("item2", 15.0)

order = Order()
order.add_item(item1, 2)
order.add_item(item2, 1)

bill_generator = BillGenerator(order)
bill_generator.generate_bill()
