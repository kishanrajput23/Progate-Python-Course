# import the utils module
import utils
print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

# Call the validate function of utils module
if utils.validate(player_hand):
    computer_hand = 1
    
    # Call the print_hand function of utils module
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')
    
    # Call the judge function of utils module
    result = utils.judge(player_hand, computer_hand)
    print('Result: ' + result)
else:
    print('Please enter a valid number')
