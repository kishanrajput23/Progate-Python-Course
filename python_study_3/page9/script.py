def validate(hand):
    if hand < 0 or hand > 2:
        return False
    # Remove else and fix indentation
    return True
        

def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

if validate(player_hand):
    print_hand(player_hand, player_name)
else:
    print('Please enter a valid number')
