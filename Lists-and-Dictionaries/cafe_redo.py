# create list called menu with items sold
menu = ["Coffee", "Tea", "Hot Chocolate", "Scone", "Biscuit", "Crisps"]


# create list called amount of item stock and convert into dict
amount = [13,8,16,24,28,8]

stock = {}

for key, value in list(zip(menu, amount)):
    stock[key] = value


# create list called value of items cost and convert into dict
cost = [2.90,2.80,4.30,1.40,1.10,2.30]

price = {}

for key, value in list(zip(menu, cost)):
    price[key] = value


# create empty variables item_value and total_stock
item_value = 0
total_stock = 0

# for loop to calculate item value and add it to total stock
for items in menu:
    item_value = ((stock.get(items) * price.get(items)))
    total_stock += (float(item_value))
total_stock = format(total_stock,".2f")
print(f"The total stock worth in the cafe is £{total_stock}.")