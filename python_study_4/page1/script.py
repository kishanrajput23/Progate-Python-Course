from menu_item import MenuItem

menu_item1 = MenuItem('Sandwich', 5)
menu_item2 = MenuItem('Chocolate Cake', 4)
menu_item3 = MenuItem('Coffee', 3)
menu_item4 = MenuItem('Orange Juice', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('Enter menu item number: '))
selected_menu_item = menu_items[order]
print('Selected item: ' + selected_menu_item.name)

count = int(input('Enter quantity (10% off for 3 or more): '))
result = selected_menu_item.get_total_price(count)
print('Your total is $' + str(result))
