class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ORDER:
    def __init__(self):
        self.its = []

    def AddItem(self, item, quantity):
        self.its.append({"i": item, "q": quantity})

    def total(self):
        total = 0
        for item in self.its:
            total += item["i"].price * item["q"]
        return total


class billgenerator:
    def __init__(self, order):
        self.order = order

    def generate_bill(self):
        total_amount = self.order.total()
        st = 0.05 * total_amount  # Assuming 5% service tax
        gst = 0.18 * total_amount  # Assuming 18% GST

        final_amount = total_amount + st + gst

        # Display the bill
        print("------ Bill ------")
        for item in self.order.its:
            print(f"{item['i'].name} x {item['q']}: {item['i'].price * item['q']}")

        print(f"\nTotal Amount: {total_amount}")
        print(f"Service Tax (5%): {st}")
        print(f"GST (18%): {gst}")
        print(f"Final Amount: {final_amount}")


# Example usage:
item1 = item("item1", 10.0)
item2 = item("item2", 15.0)

order = ORDER()
order.AddItem(item1, 2)
order.AddItem(item2, 1)

bill_generator = billgenerator(order)
bill_generator.generate_bill()
