apple_price = 2
money = 10
input_count = input('How many apples do you want?: ')
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')

if money > total_price:
    print('You have bought ' + str(count) + ' apples')
    print('You have ' + str(money - total_price) + ' dollars left')
elif money == total_price:
    print('You have bought ' + str(count) + ' apples')
    print('Your wallet is now empty')
else:
    print('You do not have enough money')
    print('You cannot buy that many apples')