import json

with open("my_backup.json", "r") as file:
    products = json.load(file)
    print("Current prices in warehouse:", products)

product_name = input("which product want with discount?")

if product_name in products:
    products[product_name] = products[product_name] - 100
    print(f"New price in python: {products[product_name]} GEL")

    with open("my_backup.json", "w") as file:
        json.dump(products, file, indent=4)
        print("File updated sucsessfully!")
else:
    print("This product is not available in the warehouse.")