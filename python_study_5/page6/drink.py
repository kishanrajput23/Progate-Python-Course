from menu_item import MenuItem

class Drink(MenuItem):
    # Define the info method
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'
    