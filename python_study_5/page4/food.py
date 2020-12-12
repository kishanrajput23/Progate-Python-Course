from menu_item import MenuItem

class Food(MenuItem):
    # Define the calorie_info method
    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))
    