class ShoppingCart:

    class Discount:
        def __init__(self, num_items, price):
            self.num_items = num_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception('Bad Item!')

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def add_discount(self, item, num_items, price):
        discount = self.Discount(num_items, price)
        self.discounts[item] = discount

    def calculate_total(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculate_item_total(item, count)
        return total

    def calculate_item_total(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.num_items:
                total += self.calculate_item_discount_total(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total

    def calculate_item_discount_total(self, item, count, discount):
        total = 0
        num_discount = count / discount.num_items
        total += num_discount * discount.price
        remaining = count % discount.num_items
        total += remaining * self.prices[item]
        return total


