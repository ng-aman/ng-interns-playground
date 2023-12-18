class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})

    def total(self):
        total = 0
        for item in self.items:
            total += item["item"].price * item["quantity"]
        return total


class Billgenerator:
    def __init__(self, order):
        self.order = order

    def generate_bill(self):
        total_amount = self.order.total()
        service_tax = 0.05 * total_amount  # Assuming 5% service tax
        gst = 0.18 * total_amount  # Assuming 18% GST

        final_amount = total_amount + service_tax + gst

        # Display the bill
        print("------ Bill ------")
        for item in self.order.its:
            print(f"{item['item'].name} x {item['quantity']}: {item['item'].price * item['quantity']}")

        print(f"\nTotal Amount: {total_amount}")
        print(f"Service Tax (5%): {service_tax}")
        print(f"GST (18%): {gst}")
        print(f"Final Amount: {final_amount}")


# Example usage:
item1 = Item("item1", 10.0)
item2 = Item("item2", 15.0)

order = Order()
order.add_item(item1, 2)
order.add_item(item2, 1)

bill_generator = Billgenerator(order)
bill_generator.generate_bill()
