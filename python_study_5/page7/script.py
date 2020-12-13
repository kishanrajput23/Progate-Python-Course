from food import Food
from drink import Drink

# Add an argument to Food()
food1 = Food('Sandwich', 5, 330)

print(food1.info())

drink1 = Drink('Coffee', 3)

drink1.volume = 180

print(drink1.info())
