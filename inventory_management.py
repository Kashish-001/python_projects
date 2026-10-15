"""
Inventory and Product Management System

Purpose:
    This program maintains a small inventory of products in a shop.
    Each product has a name, category, price and available quantity.
    The user can display all products, search a product (case-insensitive)
    and purchase it, filter costly products, view categories, add a new
    product and see a demonstration of list cloning. The program keeps
    running until the user chooses to exit.
"""

# ---------------- Constants and tuple ----------------
STORE_NAME = "Smart Mart"
# Tuple: valid menu choices (fixed values that never change)
VALID_CHOICES = ("1", "2", "3", "4", "5", "6", "7")

# ---------------- Inventory: list of dictionaries ----------------
inventory = [
    {"name": "Laptop",       "category": "Electronics", "price": 55000, "quantity": 10},
    {"name": "Mobile Phone", "category": "Electronics", "price": 20000, "quantity": 15},
    {"name": "Headphones",   "category": "Electronics", "price": 1500,  "quantity": 30},
    {"name": "Notebook",     "category": "Stationery",  "price": 60,    "quantity": 100},
    {"name": "Pen",          "category": "Stationery",  "price": 10,    "quantity": 200},
    {"name": "Rice Bag",     "category": "Grocery",     "price": 650,   "quantity": 25},
    {"name": "Sugar",        "category": "Grocery",     "price": 45,    "quantity": 50},
    {"name": "Office Chair", "category": "Furniture",   "price": 4500,  "quantity": 8},
]

# ---------------- Main program loop ----------------
while True:
    print("\n===== " + STORE_NAME + " - INVENTORY MENU =====")
    print("1. Display all products")
    print("2. Search and purchase a product")
    print("3. Show products costlier than a given price")
    print("4. Show categories and category-wise stock")
    print("5. Add a new product")
    print("6. Clone (copy) demonstration")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    # continue: skip the invalid operation and show the menu again
    if choice not in VALID_CHOICES:
        print("Invalid choice! Please try again.")
        continue

    # ---------- 1. Display all products ----------
    if choice == "1":
        print(f"\n{'No.':<5}{'Name':<15}{'Category':<14}{'Price (Rs)':>11}{'Quantity':>10}")
        print("-" * 55)
        for number, product in enumerate(inventory, start=1):
            print(f"{number:<5}{product['name']:<15}{product['category']:<14}"
                  f"{product['price']:>11}{product['quantity']:>10}")

    # ---------- 2. Search and purchase ----------
    elif choice == "2":
        # lower() makes the search case-insensitive
        search_name = input("Enter product name to search: ").strip().lower()

        found_product = None
        for product in inventory:
            if product["name"].lower() == search_name:
                found_product = product
                break                       # product found, stop searching

        if found_product is None:
            print("Product not found!")
            continue

        # dictionary method get() used to read values
        print(f"\nProduct found: {found_product.get('name')}")
        print(f"Price: Rs {found_product.get('price')}  |  "
              f"Available quantity: {found_product.get('quantity')}")

        qty_text = input("Enter number of units to purchase: ").strip()
        if not qty_text.isdigit() or int(qty_text) == 0:
            print("Invalid quantity! Enter a positive whole number.")
            continue
        units = int(qty_text)

        # Check whether sufficient stock is available
        if units > found_product["quantity"]:
            print(f"Insufficient stock! Only {found_product['quantity']} units "
                  f"available. Inventory not modified.")
        else:
            total_cost = units * found_product["price"]
            found_product["quantity"] -= units          # update inventory
            print(f"Purchase successful! Total cost = Rs {total_cost}")
            print(f"Remaining stock of {found_product['name']}: "
                  f"{found_product['quantity']}")

    # ---------- 3. List comprehension: price greater than given amount ----------
    elif choice == "3":
        limit_text = input("Enter the price limit: ").strip()
        if not limit_text.isdigit():
            print("Invalid amount! Enter a whole number.")
            continue
        limit = int(limit_text)

        costly_products = [p["name"] for p in inventory if p["price"] > limit]

        if len(costly_products) == 0:
            print(f"No product is costlier than Rs {limit}.")
        else:
            print(f"Products costlier than Rs {limit}: {costly_products}")

    # ---------- 4. Set and dictionary methods ----------
    elif choice == "4":
        categories = set()          # set stores only unique categories
        category_stock = {}         # dictionary: category -> total quantity

        for product in inventory:
            categories.add(product["category"])
            category_stock[product["category"]] = (
                category_stock.get(product["category"], 0) + product["quantity"]
            )

        print("\nUnique categories:", sorted(categories))
        print("Dictionary keys  :", list(category_stock.keys()))
        print("Category-wise stock:")
        for category, stock in category_stock.items():
            print(f"  {category:<12}: {stock} units")
        print("Total units in shop:", sum(category_stock.values()))

    # ---------- 5. Add a new product (list method append) ----------
    elif choice == "5":
        new_name = input("Enter product name: ").strip().title()
        new_category = input("Enter category: ").strip().title()
        price_text = input("Enter price: ").strip()
        qty_text = input("Enter quantity: ").strip()

        if new_name == "" or new_category == "" \
                or not price_text.isdigit() or not qty_text.isdigit():
            print("Invalid details! Product not added.")
            continue

        existing_names = [p["name"].lower() for p in inventory]
        if new_name.lower() in existing_names:
            print("Product already exists!")
            continue

        inventory.append({"name": new_name, "category": new_category,
                          "price": int(price_text), "quantity": int(qty_text)})
        print(f"{new_name} added successfully.")

    # ---------- 6. Cloning demonstration ----------
    elif choice == "6":
        original_prices = [p["price"] for p in inventory]
        prices_copy = original_prices.copy()    # clone of the list

        prices_copy.append(99999)               # modify only the copy
        prices_copy.sort()                      # sort only the copy
        removed = prices_copy.pop()             # remove last item of the copy

        print("\nOriginal list :", original_prices)
        print("Modified copy :", prices_copy)
        print("Popped value  :", removed)
        print("The original list is unchanged because only the copy was modified.")

    # ---------- 7. Exit ----------
    elif choice == "7":
        print("Thank you for using " + STORE_NAME + "!")
        break                                   # terminate the program