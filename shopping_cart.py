# shopping_cart.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

#
# INFO CAPTURE
#

total_price = 0
selected_ids = []
##id_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
valid_ids = [str(p["id"]) for p in products] # doing comparisons with string versions of these ids
print("VALID IDS:", valid_ids)

##while True:  #this will loop the program
##    selected_id = input("Please input a product identifier: ")  #this is a string 
##    if selected_id == "DONE" or selected_id == "done" or selected_id == "Done" :
##        break   #this ends the loop
##    else:
##        #matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
##        #matching_product = matching_products[0]
##        #total_price = total_price + matching_product["price"]
##        #print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))
##        selected_ids.append(selected_id)
##    if selected_id not in str(id_list):
##        print("PLEASE START OVER USING CORRECT PRODUCT ID")
##        exit()

while True:
    selected_id = input("Please input a product identifier, or 'DONE': " ) # the data input will always be a str

    if selected_id == "DONE" or selected_id == "done" or selected_id == "Done":
        break # stops the loop
    elif str(selected_id) in valid_ids:
        selected_ids.append(selected_id)
    else:
        print("OH, detected invalid input! Please try again...")
        next # proceeds into the next iteration of the loop (OK to omit in this basic example because there is no more code following it inside the loop before the loop repeats)

print("SELECTED IDS:", selected_ids)
    
#
# INFO DISPLAY
#

#print(selected_ids)

import datetime
now = datetime.datetime.now()

print("---------------------")
print("GARGIULO'S MEAT MARKET")
print("631-422-2020")
print("GARGIULOSMEATMARKET.COM")
print("---------------------")
print ("CHECKOUT AT" + " " + now.strftime("%Y-%m-%d %H:%M"))   #https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
print("---------------------")

print("SELECTED PRODUCTS:")

for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        total_price = total_price + matching_product["price"]
        price_usd = "${0:.2f}".format(matching_product["price"])   #this line coverts price format
        print("    " + matching_product["name"] + " " + str(price_usd))
        
print("---------------------")
subtotal = ("${0:.2f}".format(total_price))
print("SUBTOTAL: " + str(subtotal))
tax = .08875 * total_price
print("TAX: " + str("${0:.2f}".format(tax)))
total = total_price + tax
print("TOTAL: " + str("${0:.2f}".format(total)))

print("---------------------")

print("THANK YOU HOPE TO SEE YOU AGAIN SOON!")

print("---------------------")
