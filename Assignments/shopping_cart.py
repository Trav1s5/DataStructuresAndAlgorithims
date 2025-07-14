class ShoppingCart:
    def __init__(self):
        self.items = []  # List of (item_name, qty)
        self.discount = 0  # Discount in percentage

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def set_discount(self, discount_percent):
        if 0 <= discount_percent <= 100:
            self.discount = discount_percent
        else:
            print("Invalid discount. Must be between 0 and 100.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        if self.discount > 0:
            total = total * (1 - self.discount / 100)
        return total


# === Usage Example ===
cart = ShoppingCart()

# Add items to cart
cart.add_item("Kiwi", 160)
cart.add_item("Orange", 190)
cart.add_item("Passive", 76)

# Set a discount
cart.set_discount(10)  # 10% discount

# Display cart contents
print("\nCurrent items in cart:")
for item in cart.items:
    print(f"{item[0]} - {item[1]}")

# Calculate and show total after discount
total_qty = cart.calculate_total()
print(f"\nTotal quantity after discount: {total_qty:.2f}")
