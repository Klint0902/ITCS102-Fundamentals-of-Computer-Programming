name = input("Enter your name: ")
type = input("Enter the type of item: ")
isFragile = bool(input("Is the item fragile? "))
weight = float(input("Enter the weight of the item (kg): "))
distance = float(input("Enter the item's ditance to be covered (km): "))
is_express = bool(input("Is the delivery Express? "))
is_international = bool(input("Is the delivery International? "))

base_cost = (weight * 2.5) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


print("================================ TOTAL COST ================================")
print("Total price: PHP", total)