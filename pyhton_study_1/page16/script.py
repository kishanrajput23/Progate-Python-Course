apple_price = 2

# Receive the number of apples by using input(), and assign it to the input_count variable 
input_count = input("How many apples do you want?: ")

# Convert the input_count variable to an integer, and assign it to the count variable
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')