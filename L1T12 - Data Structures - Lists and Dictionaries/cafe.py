# Create a menu list with available items
menu = ['Latte', 'Espresso', 'cake', 'tea']

# Create a dictionary 'stock' with the quantity of each item in stock
stock = {
    'Latte': 14 ,
    'Espresso': 23 ,
    'cake': 10 ,
    'tea': 12
}

# Create a dictionary 'price' with the price of each item
price = {
    'Latte': 3 ,
    'Espresso': 3.5 ,
    'cake': 2.75 ,
    'tea': 2.5
}

total_stock = 0

# Iterate through each item in the 'menu' and calculate the value of each item by multiplying stock by price
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value 
    
print (total_stock)    
    

