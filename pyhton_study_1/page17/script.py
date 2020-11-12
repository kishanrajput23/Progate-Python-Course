apple_price = 2
# Assign 10 to the money variable
money = 10

input_count = input('How many apples do you want?: ')
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')

left_money = money - total_price
# Add control flow based on the comparison of money and total_price
if money > total_price:
    print("You have bought " + str(count) + " apples")
    print("You have " + str(left_money) + " dollars left")
    
elif money == total_price:
    print("You have bought " + str(count) + " apples")
    print("Your wallet is now empty")
    
else:
    print("You do not have enough money")
    print("You cannot buy that many apples")