numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    # Skip the loop for numbers divisible by 3
    if number % 3 == 0:
        continue
    
    print(number)