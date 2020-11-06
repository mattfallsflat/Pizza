#Pizza Maker
class pizza:
    toppings = ""
    crust_type = ""
    sauce_type = ""
    cheese_type = ""

    def __init__(self, toppings, crust_type, sauce_type, cheese_type):
        toppings = toppings
        crust_type = crust_type
        sauce_type = sauce_type
        cheese_type = cheese_type
    def get_pizza(self):
        return self.toppings
        return self.crust_type
        return self.sauce_type
        return self.cheese_type
     
crusts = ["white crust", "White Crust", "Wheat Crust", "wheat crust"]
cheeses = ["American Cheese", "american cheese", "American cheese", "Russian Cheese", "russian cheese", "Russian cheese"]
sauces = ["Pesto Sauce", "Tomato Sauce", "pesto sauce", "tomato sauce"]
toppings = ["Pepperoni", "pepperoni", "Mushrooms", "mushrooms", "Jalepeno", "jalepeno", "No toppings", "no toppings"]
print("Welcome to create your own pizza!")
print("Please pick a type of crust you want for your pizza and make sure it is one of the choices!")
print("Do you want White Crust or Wheat Crust?")
crust = input("Please enter the crust you want for your pizza: ")
while crust not in crusts:
    crust = input("Please type one of the choices: ")
    continue 
if crust in crusts:
    print("Please pick the cheese you want for the pizza!")
    print("Do you want American Cheese or Russian Cheese?")
    cheese = input("Please enter the cheese you want for the pizza:  ")
    while cheese not in cheeses:
        cheese = input("Please type one of the choices: ")
        continue
    if cheese in cheeses:
        print("Please pick a sauce you want for the pizza!")
        print("Do you want Pesto Sauce or Tomato Sauce?")
        sauce = input("Please enter the sauce you want for the pizza:  ")
        while sauce not in sauces:
            cheese = input("Please type one of the choices: ")
            continue
        if sauce in sauces:
          print("Please pick the toppings you want for the pizza!")
          print("Do you want Pepperoni, Mushrooms, Jalepeno or no toppings?")
          top = input("Please enter the toppings you want for the pizza:  ")
          while top not in toppings:
             top = input("Please type one of the choices: ")
          if top in toppings:
              pizza1 = pizza(top, crust, sauce, cheese)
              print("Great job! Here is your pizza!")
              print(pizza1.get_pizza())
           
               
        
    

    

