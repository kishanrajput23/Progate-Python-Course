# Assign 20 to the money variable
money = 20

items = {'apple': 2, 'banana': 4, 'orange': 6}
for item_name in items:
    print('--------------------------------------------------')
    # Using the money variable, print 'You have ___ dollars in your wallet'
    print("You have "+ str(money) +" dollars in your wallet")
    
    print('Each ' + item_name + ' costs ' + str(items[item_name]) + ' dollars')
    
    input_count = input('How many ' + item_name + 's do you want?: ')
    print('You will buy ' + input_count + ' ' + item_name + 's')
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('The total price is ' + str(total_price) + ' dollars')
    
    # Add control flow based on the comparison of money and total_price
    if money >= total_price:
        print("You have bought "+ input_count + " " + item_name + "s")
        money -= total_price
    else:
        print("You do not have enough money")
        print("You cannot buy that many " + item_name + "s")