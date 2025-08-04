items_needed = ["milk", "egg", "bread", "butter", "rice", "pepper_p", "water"]
pantry_items = ["pepper_p", "water"]
shopping_list =[item for item in items_needed if item not in pantry_items]
print ("you need to buy:")
for item in shopping_list:
    print(" ", item)


