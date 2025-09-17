# Function to calculate total cost after adding tax

def calculate_total(price, tax=5):
    return price + (price * tax / 100)


print(calculate_total(100))


# Program to modify a global list by adding new items

items = []

def add_item(item):
    global items
    items.append(item)


add_item("apple")

print(items)
