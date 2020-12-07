class MenuItem:
    def __init__(self):
        # Set self.name to 'Sandwich'
        self.name = "Sandwich"
        
        # Set self.price to 5
        self.price = 5

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
# Delete the following two lines


print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('Your total is $' + str(result))
