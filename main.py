name = "Vato Ephenia"
learning_months = 18
course_duration_years = 1.5
is_student = True

print(f"name is: {name} and its type is: {type(name)}")
print(f"Month is: {learning_months} and its type is: {type(learning_months)}")
print(f"Years is: {course_duration_years} and its type is: {type(course_duration_years)}")
print(f"Is student? {is_student} and its type is: {type(is_student)}")

age_text = 25
age_plus_one = age_text + 1
age_number = int(age_text)

print(f"Original type: {type(age_text)}")
print(f"New type: {type(age_number)}")
print(f"Next year I will be: {age_number + 1}")

inventory = ["iphone15", "macbook air", "airpods pro"]

print(f"inventory list: {inventory}")
print(f"type of inventory: (type{inventory})")

# 0 = iphone 15, 1 = macbook air, 2 = airpods pro 
print(f"firs item in store: {inventory[0]}")
inventory.append("apple watch")
print(f"updated inventory: {inventory}")

total_items = len(inventory)
has_iphone_15 = True
print(f"second item in store: {inventory[1]}")
print(f"total numbers of items in inventory: {total_items}")
print(f"has_iphone_15? {has_iphone_15} and its type is: {type(has_iphone_15)}")

iphone_15_stock = 0
costumer_wants = 1
if iphone_15_stock >= costumer_wants:
    print("sales succesful! processing order...")
    iphone_15_stock = iphone_15_stock - costumer_wants
    print(f"remaining stok: {iphone_15_stock}")
else:
    print("sorry, we are out of stock!")

price = 100
quantity = 3
if quantity > 5:
    print("you got 20% discount!")
elif quantity >= 2:
    print("you got 10% discount!")
else:
    print("no discount this time.")

if is_student == True and quantity>2:
    print("special student offer: you got free screen protector!")
else:
    print("regular order processing.")

city = "Batumi"
total_price = 150
if city == "Tbilisi" or total_price > 100:
    print("free shipping activated!")
else:
    print("shipping cost: 5 GEL")

is_employee = False
position = "Manager"
if is_employee:
    print("welcome to the system!")
    if position == "Manager":
        print("acces granted to all financial reports.")
    else:
        print("acces granted only to inventory stock")
else:
    print("acess denied! you are not our an employee.")

items = ["iphone 15", "macbook air", "airpods pro", "apple watch"]
print("cheking store inventory:")
for item in items:
    print(f"product in stock: {item}")

prices = [100, 250, 500]
for price in prices:
    print(f"price tag: {price} GEL")




