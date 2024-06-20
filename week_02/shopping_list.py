grocery_list = ()
grocery_history = []
grand_total = 0
item_total = 0
total_quantity=0

while True:
    name = input("Name(q to quit):")
    if name.lower() == "q":
        break
    else:
        cost = input("Price: ")
    quantity = input("Quantity: ")
    grocery_list = {'item_name': name, 'quantity': int(quantity), 'cost': float(cost)}
    grocery_history.append(grocery_list)

print("\n PRINTING GROCERY LIST...  \n")
for item in grocery_history:
    print(item)


for item in grocery_history:
    item_total = item['quantity'] * item['cost']
    grand_total += item_total
    total_quantity += item['quantity']


print("Total number of items purchased:", total_quantity)
print("Your weekly shopping cost: ", grand_total)


