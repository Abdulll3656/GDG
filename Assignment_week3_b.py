
Groceries = []
prices = []
Total = 0

while True:
    item = input("Enter an item you'd like to buy or q to quit:")
    if item.lower() == "q":
       break
    else:
       price = input(f"Enter the price of a {item}: $")
       Groceries.append(item)
       prices.append(price)
print("____Your cart____")
for Grocery in Groceries:
       print(Grocery.title(), end = " ")
for price in prices:
       Total += int(price)

print()
print(f"Your total amount is : ${Total}")













