# Import the Food class and Drink class
from food import Food
from drink import Drink

# Create an instance of the Food class and assign it to the food1 variable
food1 = Food("Sandwich", 5)

# Call the info method from food1 and output the return value
print(food1.info())

# Create an instance of the Drink class and assign it to the drink1 variable
drink1 = Drink("Coffee", 3)

# Call the info method from drink1 and output the return value
print(drink1.info())
