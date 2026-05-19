import json
with open("my_backup.json") as file:
    products = json.load(file)

def calculate_tax(price):
    return price * 0.18
def apple_discount(price, percent):
    return price - (price * (percent / 100))
while True:
    print("\n--- APPLE TECH STORE ---")
    print("1. View Inventory")
    print("2. Buy Products")
    print("3. Admin panel")
    print("4. Exit")

    choise = input("Choose an option (1-4):")

    if choise == "1":
        print("\nOur current stock and prices:")
        for item, info in products.items():
            name = item.replace('_', ' ').title()
            print(f"{name} - price: {info['price']} GEL | stock: {info['quantity']} pcs")
    
    elif choise == "2":
        user_input = input("Enter product name: ").replace(" ", "_").lower()

        if user_input in products:
            if products[user_input]["quantity"] > 0:
                base_price = products[user_input]["price"]

                if base_price > 1000:
                    final_price = apple_discount(base_price, 10)
                    print("You got a 10% loyalty discount for premium product!")
                else: 
                    final_price = base_price
                tax = calculate_tax(final_price)

                print(f"Base price: {base_price} GEL")
                print(f"Final price (with discount): {final_price} GEL")
                print(f"Tax included (18% VAT): {tax} GEL")

                products[user_input]["quantity"] -= 1

                with open ("my_backup.json", "w") as file:
                    json.dump(products, file, indent=4)

                print("Order processed successfully! Stock updated.")
            else:
                print("Sorry, this product is out of stock!")
        else:
            print(f"Sorry, we don't have {user_input} in stock.")

    elif choise == "3":
        password = input("Enter admin password: ")

        if password == "1234":
            print("\n--- Welcome to Admin Panel ---")
            while True:
                print("\nAdmin Options:")
                print("1. Restock Product")
                print("2. Back to Main Menu")

                admin_choise = input("Chose admin option (1-2): ")

                if admin_choise == "1":
                    prod_name = input("Enter product name to restock (e. g. iphone_15): ").replace(" ", "_").lower()

                    if prod_name in products:
                        amount = int(input("How mane pieces are you adding to stock?:"))
                        products[prod_name]["quantity"] += amount
                        with open("my_backup.json", "w") as file:
                            json.dump(products, file, indent=4)

                        print(f"Successfully added {amount} pcs to {prod_name.replace('_', ' ').title()}!")
                    else:
                        print("This product doesn't exist in our base!")
                elif admin_choise == "2":
                    print("Exist Admin  Panel...")
                    break
                else:
                    print("Invalid admin option!")
        else:
            print("Acces Denied! Incorrect Password.")
       
    elif choise == "4":
        print("Thank you for using Apple tech store! Goodbye.")
        break
    else:
        print("Invalid option! Please choose 1, 2, 3 or 4.")

