from menu_item import MenuItem

menu_item1 = MenuItem('Sandwich', 5)
menu_item2 = MenuItem('Chocolate Cake', 4)
menu_item3 = MenuItem('Coffee', 3)
menu_item4 = MenuItem('Orange Juice', 2)

# Set the menu_items variable to a list of the MenuItem instances
menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# Create the for loop
for menu_item in menu_items:
    print(menu_item.info())
