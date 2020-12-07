class MenuItem:
    # Define the __init__ method
    def __init__(self):
        print("An instance of the MenuItem class was created!")

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'Sandwich'
menu_item1.price = 5

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('Your total is $' + str(result))
