# lesson 7
foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy or press q to quit. ")
    if food.lower() == "q":
        break
    else:
        price = float(input("enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)

print("****** YOUR CART ******")    

for food in foods:
    print(food)
    
for price in prices:
    total += price  

print("")
print(f"Your total is: R{total}")      