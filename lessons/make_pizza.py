"""Practice Instantiating Pizza class"""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)

print(Pizza)
print(my_pizza)
print(my_pizza.size)
print(my_pizza.toppings)
print(my_pizza.gluton_free)

sals_pizza: Pizza = Pizza("small", 2, False)
print(sals_pizza.price())

# def price(pizza_order: Pizza) -> float:
#     """Calculate and return cost of pizza"""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else:
#         cost =5.0
#     #charge .75 for each topping
#     cost += 0.75 * pizza_order.toppings
#     #charge 1.00 for gluton free
#     if pizza_order.gluton_free == True:
#         cost += 1.0
#     return cost

print(my_pizza.toppings)
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())


