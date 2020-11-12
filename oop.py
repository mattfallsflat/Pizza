#Pizza Maker
class pizza:
    toppings = ""
    crust_type = ""
    sauce_type = ""
    cheese_type = ""

    def __init__(self, toppings, crust_type, sauce_type, cheese_type):
        self.toppings = toppings
        self.crust_type = crust_type
        self.sauce_type = sauce_type
        self.cheese_type = cheese_type
    def get_toppings(self):
        return self.toppings
    def get_cheese(self):
        return self.cheese_type
    def get_crust(self):
        return self.crust_type
    def get_sauce(self):
        return self.sauce_type
        
     
crusts = ["white crust", "White Crust", "Wheat Crust", "wheat crust"]
cheeses = ["American Cheese", "american cheese", "American cheese", "Russian Cheese", "russian cheese", "Russian cheese"]
sauces = ["Pesto Sauce", "Tomato Sauce", "pesto sauce", "tomato sauce"]
toppings = ["Pepperoni", "pepperoni", "Mushrooms", "mushrooms", "Jalepeno", "jalepeno", "No toppings", "no toppings"]
print("Welcome to create your own pizza!")
print("Please pick a type of crust you want for your pizza and make sure it is one of the choices!")
print("Do you want White Crust or Wheat Crust?")
crust = input("Please enter the crust you want for your pizza: ")
cheese = input("Please enter the cheese you want for the pizza:  ")
sauce = input("Please enter the sauce you want for the pizza:  ")
top = input("Please enter the toppings you want for the pizza:  ")

pizza1 = pizza(top, crust, sauce, cheese)
print("Great job! Here is your pizza!")
print(pizza1.get_toppings())
print(pizza1.get_cheese())
print(pizza1.get_sauce())
print(pizza1.get_crust())


