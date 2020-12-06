class MenuItem:
    def info(self):
        return self.name + ': $' + str(self.price)

    # Define the get_total_price method
    def get_total_price(self, count):
        total_price = self.price * count
        return total_price

menu_item1 = MenuItem()
menu_item1.name = 'Sandwich'
menu_item1.price = 5

print(menu_item1.info())

# Call the get_total_price method
result = menu_item1.get_total_price(4)

# Output 'Your total is $____'
print("Your total is $ "+ str(result))
