class Product:
    def __init__(self, name, price, availability=True):
        self.name = name
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"Товар: {self.name}, Ціна: {self.price}, Доступність: {'Є в наявності' if self.availability else 'Немає'}"

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.availability:
            self.items.append(product)
        else:
            print(f"Товар {product.name} немає в наявності.")

    def remove_product(self, name):
        self.items = [item for item in self.items if item.name != name]

    def total_price(self):
        return sum(item.price for item in self.items)

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
        for item in self.items:
            print(item)

product1 = Product("Ноутбук", 15000)
product2 = Product("Миша", 500)
product3 = Product("Навушники", 3000, availability=False)
cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
cart.show_cart()
print(f"Загальна вартість: {cart.total_price()} грн")


