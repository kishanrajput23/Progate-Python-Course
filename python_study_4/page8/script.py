class MenuItem:
    def info(self):
        # Return the contents of print() as a return value
        return self.name + ': $' + str(self.price)


menu_item1 = MenuItem()
menu_item1.name = 'Sandwich'
menu_item1.price = 5

# Output the value of menu_item1.info()
print(menu_item1.info())

menu_item2 = MenuItem()
menu_item2.name = 'Chocolate Cake'
menu_item2.price = 4

# Output the value of menu_item2.info()
print(menu_item2.info())
