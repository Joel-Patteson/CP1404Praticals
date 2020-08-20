list= []
num_items = int(input("Enter the number of items: "))
while num_items<0:
    print("invalid value")
    num_items = int(input("Enter the number of items: "))

for i in range(0, num_items):
    price = float(input("Enter the price of item: "))
    while price <= 0:
        print("Invalid value")
        price = float(input("Enter the price of item: "))
    list.append(price)
total = sum(list)

if total > 100:
    final_price = total * 0.9
    print("Total price for ", num_items, "items is $", final_price)
else:
    print("Total price for", num_items, "items is $", total)