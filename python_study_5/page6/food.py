from menu_item import MenuItem
class Food(MenuItem):
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
    
    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))