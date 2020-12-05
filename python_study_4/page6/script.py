class MenuItem:
    # Define the info method
    def info(self):
        print("Display menu item name and price")


menu_item1 = MenuItem()
menu_item1.name = 'Sandwich'
menu_item1.price = 5

# Call the info method from menu_item1
menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'Chocolate Cake'
menu_item2.price = 4

# Call the info method from menu_item2
menu_item2.info()
