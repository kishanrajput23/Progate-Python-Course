from menu_item import MenuItem

class Food(MenuItem):
    # Define the __init__ method
    def __init__(self, name, price, calorie_count):
        self.name = name
        self.price = price
        self.calorie_count = calorie_count
    
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
    
    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))