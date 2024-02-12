# create the toppings and prices list 
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# .count() how many $2 pizzas there are and print it out
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

# print the string "We sell ___ different kids of pizza!" with information about # of options with len()
num_pizzas = len(toppings)
#print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# create two-dimensional (2D) lists called pizza_and_prices with each sublist in this list having one pizza and one associated price
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#print(pizza_and_prices)

# sort the 2D list in the order of increasing prices (ascending)
pizza_and_prices.sort()
#print(pizza_and_prices)

# store the first element of the 2D list as the cheapeast_pizza
cheapest_pizza = pizza_and_prices[0]

# store the last item in the list as the most expensive pizza
priciest_pizza = pizza_and_prices[-1]

# remove the last item in the list because someone came in and said they want the most expensive pizza
pizza_and_prices.pop(-1)
#print(pizza_and_prices)

# add a new pizza to the list using .insert() to make sure it's in the right place in the order
pizza_and_prices.insert(2, [2.5, "peppers"])

# create a new variable with the three cheapest pizzas
three_cheapest = pizza_and_prices[-3:]
# print the three cheapest pizzas
print(three_cheapest)






#print(pizza_and_prices)