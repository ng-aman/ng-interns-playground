class i:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ORDER:
    def __init__(self):
        self.its = []

    def Add_item(self, item, quantity):
        self.its.append({"i": item, "q": quantity})

    def total(self):
        t = 0
        for item in self.its:
            t += item["i"].price * item["q"]
        return t


class billgenerator:
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
            print(f"{item['i'].name} x {item['q']}: {item['i'].price * item['q']}")

        print(f"\nTotal Amount: {total_amount}")
        print(f"Service Tax (5%): {service_tax}")
        print(f"GST (18%): {gst}")
        print(f"Final Amount: {final_amount}")


# Example usage:
item1 = i("item1", 10.0)
item2 = i("item2", 15.0)

order = ORDER()
order.Add_item(item1, 2)
order.Add_item(item2, 1)

bill_generator = billgenerator(order)
bill_generator.generate_bill()

