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
    print("3. Exit")

    choise = input("Choose an option (1-3):")

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
    elif choise == 3:
        print("Thank you for using Apple tech store! Goodbye.")
        break
    else:
        print("Invalid option! Please choose 1, 2 or 3.")

