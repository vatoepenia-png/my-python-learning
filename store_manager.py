products = {
    "iphone_15": 2500,
    "macbook_air": 4000,
    "airpods_pro": 700,
    "apple_watch": 900
}

def calculate_tax(price):
    return price * 0.18

def apply_discount(price, percent):
    return price - (price * (percent / 100))

while True:
    print("\n--- APPLE TECH STORE ---")
    print("1. View Inventory")
    print("2. Buy Product")
    print("3. Exit")
    
    choise = input("Choose an option (1-3): ")
    
    if choise == "1":
        print("\nOur current stock and prices:")
        for item, price in products.items():
            print(f"{item.replace('_', ' ').title()}: {price} GEL")
            
    elif choise == "2":
        user_input = input("Enter product name: ").replace(" ", "_").lower()
        
        if user_input in products:
            base_price = products[user_input]
            
            if base_price > 1000:
                final_price = apply_discount(base_price, 100)  
                print("You got a 10% loyalty discount for premium product!")
            else:
                final_price = base_price
                
            tax = calculate_tax(final_price)
            
            print(f"Base price: {base_price} GEL")
            print(f"Final price (with discount): {final_price} GEL")
            print(f"Tax included (18% VAT): {tax} GEL")
            print("Order processed successfully!")
        else:
            print(f"Sorry, we don't have {user_input} in stock.")
            
    elif choise == "3":
        print("Thank you for using Apple tech store! Goodbye.")
        break
    else:
        print("Invalid option! Please choose 1, 2 or 3.")

