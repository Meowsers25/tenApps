import random

print('------------------------------------------')
print('          ROCK PAPER SCISSORS')
print('------------------------------------------')
print()

player_choice = input('Choose rock, paper, or scissors: ')
print(player_choice)

turn_choice = random.choice(['rock', 'paper', 'scissors'])
print(turn_choice)


if player_choice == 'rock' and turn_choice == 'rock':
    print('It\'s a tie!')
elif player_choice == 'rock' and turn_choice == 'paper':
    print('You lose. Paper covers rock.')
elif player_choice == 'rock' and turn_choice == 'scissors':
    print('You win! Rock crushes scissors')
elif player_choice == 'paper' and turn_choice == 'rock':
    print('You win! Paper covers rock!')
elif player_choice == 'paper' and turn_choice == 'paper':
    print('It\'s a tie.....')
elif player_choice == 'paper' and turn_choice == 'scissors':
    print('You lose, scissors cut paper.')
elif player_choice == 'scissors' and turn_choice == 'rock':
    print('You lose, rock crushes scissors.')
elif player_choice == 'scissors' and turn_choice == 'paper':
    print('You win! Scissors cut paper!')
elif player_choice == 'scissors' and turn_choice == 'scissors':
    print('It\'s a tie.....')
else:
    print('Invalid entry.')

