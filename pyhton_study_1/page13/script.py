money = 2
apple_price = 2

if money > apple_price:
    print('You can buy an apple')
# When the two variables have the same value, print 'You can buy an apple but your wallet is now empty'
elif money == apple_price:
    print("You can buy an apple but your wallet is now empty")

else:
    print('You do not have enough money')
