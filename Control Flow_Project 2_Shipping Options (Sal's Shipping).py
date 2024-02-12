#create a variable that is initialized with the weight of a package
weight = 41.5

#print Ground Shipping options based on weight
print("Ground Shipping: ")
if weight <= 2:
  print(weight * 1.5 + 20)
elif weight <= 6:
  print(weight * 3.0 + 20)
elif weight <= 10:
  print(weight * 4.0 + 20)
else:
  print(weight * 4.75 + 20)

#print the fixed Premium Shipping option
premium_cost = 125.00
print("Premium Shipping: ")
print(premium_cost)

#print the Drone Shipping options based on weight
print("Drone Shipping: ")
if weight <= 2:
  print(weight * 4.5)
elif weight <= 6:
  print(weight * 9.0)
elif weight <= 10:
  print(weight * 12)
else:
  print(weight * 14.25)

# when weight is 4.8, ground shipping is the cheapest at $34.40
# when weight is 41.5, premium shipping is the cheapest at $125.00