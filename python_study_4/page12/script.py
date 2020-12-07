class MenuItem:
    # Add the parameters name and price
    def __init__(self, name, price):
        # Set this to the name argument instead of 'Sandwich'
        self.name = name
        
        # Set this to the price argument instead of 5
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


# Add 'Sandwich' and 5 as arguments
menu_item1 = MenuItem("Sandwich", 5)

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('Your total is $' + str(result))
