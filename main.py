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
