# core/product_manager.py

class Product:
    def __init__(self, product_id, name, price_inr):
        self.product_id = product_id
        self.name = name
        self.price_inr = price_inr

    def display_details(self):
        return f"Product[ID={self.product_id}, Name={self.name}, Price={self.price_inr} INR]"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to inventory.")

    def get_total_value(self):
        total = sum(p.price_inr for p in self.products)
        return total
