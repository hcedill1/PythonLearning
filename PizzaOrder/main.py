print("Welcome to Python Pizza Deliveries!!\n")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
size = input("What size pizza do you want? S,M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

if(size == "S"):
    your_pizza_price = 15
    if(add_pepperoni == "Y"):
        your_pizza_price = your_pizza_price + 2
    else:
        your_pizza_price = your_pizza_price + 0   
elif(size == "M"):
    your_pizza_price = 20
    if(add_pepperoni == "Y"):
        your_pizza_price = your_pizza_price + 3
    else: 
        your_pizza_price = your_pizza_price + 0
else:
    your_pizza_price = 25
    if(add_pepperoni == "Y"):
        your_pizza_price = your_pizza_price + 3
    else: 
        your_pizza_price = your_pizza_price + 0


if(extra_cheese == "Y"):
    your_pizza_price = your_pizza_price + 1
else:
    your_pizza_price = your_pizza_price + 0


print(f"You final bill is: ${your_pizza_price}")



