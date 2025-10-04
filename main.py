# main.py
from core import product_manager
from core import logistics

if __name__ == "__main__":
    # 1. Create products
    p1 = product_manager.Product("P001", "Laptop", 60000)
    p2 = product_manager.Product("P002", "Phone", 20000)

    # 2. Create Inventory and add products
    inventory = product_manager.Inventory()
    inventory.add_product(p1)
    inventory.add_product(p2)

    print("\n--- Inventory Summary ---")
    for prod in inventory.products:
        print(prod.display_details())
    print("Total Inventory Value:", inventory.get_total_value(), "INR")

    # 3. Create DeliveryTruck
    truck = logistics.DeliveryTruck("V001", capacity_kg=2, license_plate="MH-12-AB-1234")

    print("\n--- Truck Summary Before Loading ---")
    print(truck.display_summary())

    # 4. Load products
    truck.load_products(inventory.products)

    print("\n--- Truck Summary After Loading ---")
    print(truck.display_summary())

