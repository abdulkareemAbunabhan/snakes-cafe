welcomeMsg = """ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""

appetizers = ["wings","cookies","spring solls"]

entrees = ["salmon","steak","meat mornado","a literal garden"]

desserts = ["ice cream","cake","pie"]

drinks = ["coffee","tea","unicorn tears"]


makeOrder= """***********************************
** What would you like to order? **
***********************************"""

print(welcomeMsg)
print('')

print("Appetizers")
print("----------")
for item in appetizers:
    print(item)

print('')
print("Entrees")
print("----------")
for item in entrees:
    print(item)

print('')
print("Desserts")
print("----------")
for item in desserts:
    print(item)

print('')
print("Drinks")
print("----------")
for item in drinks:
    print(item)

print(makeOrder)



order=""
arr=[]
while order !='quit':
    order=input("> ")
    if order !='quit':
        if order.lower() in appetizers or order in entrees or order in desserts or order in drinks :
            arr.append(order)
            print(f" {arr.count(order)} order of {order} has been added to your meal ")
        else: print(f"this order {order} is not available now")


print("you'r list orders are " ,arr)

