"""
Inventory and Product Management System

Purpose:
    Maintains a small shop inventory (name, category, price, quantity).
    The user can display products, search (case-insensitive) and buy a
    product, filter costly products, view unique categories and see a
    list-cloning demo. The program runs until the user chooses to exit.
"""

# Tuple of valid menu choices (fixed values)
CHOICES = ("1", "2", "3", "4", "5")

# Inventory: list of dictionaries (8 products)
inventory = [
    {"name": "Laptop",       "category": "Electronics", "price": 55000, "quantity": 10},
    {"name": "Mobile Phone", "category": "Electronics", "price": 20000, "quantity": 15},
    {"name": "Headphones",   "category": "Electronics", "price": 1500,  "quantity": 30},
    {"name": "Notebook",     "category": "Stationery",  "price": 60,    "quantity": 100},
    {"name": "Pen",          "category": "Stationery",  "price": 10,    "quantity": 200},
    {"name": "Rice",     "category": "Grocery",     "price": 650,   "quantity": 25},
    {"name": "Sugar",        "category": "Grocery",     "price": 45,    "quantity": 50},
    {"name": "Chair", "category": "Furniture",   "price": 4500,  "quantity": 8},
]

while True:
    print("\n1. Display products  2. Search & buy  3. Costly products  "
          "4. Categories & clone demo  5. Exit")
    choice = input("Enter choice (1-5): ").strip()

    if choice not in CHOICES:            # skip invalid choice
        print("Invalid choice!")
        continue

    if choice == "1":                    # display all products
        for p in inventory:
            print(f"{p['name']:<14}{p['category']:<13}Rs {p['price']:<7} Qty: {p['quantity']}")

    elif choice == "2":                  # search and purchase
        name = input("Enter product name: ").strip().lower()   # case-insensitive
        found = None
        for p in inventory:
            if p["name"].lower() == name:
                found = p
                break                    # stop searching once found
        if found is None:
            print("Product not found!")
            continue

        print("Price:", found.get("price"), "| Quantity:", found.get("quantity"))
        units = input("Units to purchase: ").strip()
        if not units.isdigit() or int(units) == 0:
            print("Invalid quantity!")
            continue
        units = int(units)

        if units > found["quantity"]:    # stock check
            print("Insufficient stock! Inventory not modified.")
        else:
            found["quantity"] -= units   # update inventory
            print("Total cost: Rs", units * found["price"])

    elif choice == "3":                  # list comprehension
        limit = input("Enter price limit: ").strip()
        if not limit.isdigit():          # skip invalid amount
            print("Invalid amount!")
            continue
        limit = int(limit)
        print([p["name"] for p in inventory if p["price"] > limit])

    elif choice == "4":
        print("Categories:", set(p["category"] for p in inventory))   # set
        print("Product fields:", list(inventory[0].keys()))           # dict method

        prices = [p["price"] for p in inventory]
        prices_copy = prices.copy()      # clone of the list
        prices_copy.append(99999)        # modify only the copy
        prices_copy.sort()
        print("Original:", prices)
        print("Copy    :", prices_copy)
        print("Original list is unchanged; only the copy was modified.")

    else:                                # choice == "5"
        print("Thank you!")
        break                            # terminate the program