"""Define Pizza class"""

class Pizza:

    #attributes
    size: str          #"small" or "large"
    toppings: int      #number of toppings
    gluton_free: bool  #True if yes, False if no

    def __init__(self, size_input: str, toppings_input: int, gluton_free_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.gluton_free = gluton_free_input
        #it actually returns self 

    def price(self) -> float:
        """Calculate and return cost of pizza"""
        cost: float = 0.0
        if self.size == "large":
            cost = 6.0
        else:
            cost =5.0
        #charge .75 for each topping
        cost += 0.75 * self.toppings
        #charge 1.00 for gluton free
        if self.gluton_free == True:
            cost += 1.0
        return cost
    

    def add_toppings(self, num_toppings: int) -> None:
        """Add a certain number of toppings"""
        self.toppings += num_toppings