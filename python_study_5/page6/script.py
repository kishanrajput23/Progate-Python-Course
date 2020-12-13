from food import Food
from drink import Drink

food1 = Food('Sandwich', 5)
food1.calorie_count = 330
print(food1.info())

# Create an instance of the Drink class and assign it to the drink1 variable
drink1 = Drink("Coffee", 3)

# Set the volume variable of drink1 to 180
drink1.volume = 180

# Call the info method from drink1 and output the return value
print(drink1.info())
