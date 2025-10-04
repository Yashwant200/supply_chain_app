# core/logistics.py
from core.product_manager import Product

class Vehicle:
    def __init__(self, vehicle_id, capacity_kg):
        self.vehicle_id = vehicle_id
        self.capacity_kg = capacity_kg
        self.loaded_products = []

    def get_details(self):
        return f"Vehicle[ID={self.vehicle_id}, Capacity={self.capacity_kg}kg]"


class DeliveryTruck(Vehicle):
    def __init__(self, vehicle_id, capacity_kg, license_plate):
        super().__init__(vehicle_id, capacity_kg)
        self.license_plate = license_plate

    def load_products(self, products):
        # Assume each product weighs 0.5kg
        total_weight = len(products) * 0.5
        if total_weight <= self.capacity_kg:
            self.loaded_products.extend(products)
            print(f"Loaded {len(products)} products into truck {self.license_plate}.")
        else:
            print(f"Error: Over capacity! Truck capacity is {self.capacity_kg}kg, but tried to load {total_weight}kg.")

    def display_summary(self):
        return (f"DeliveryTruck[ID={self.vehicle_id}, Plate={self.license_plate}, "
                f"Capacity={self.capacity_kg}kg, Loaded={len(self.loaded_products)} items]")
