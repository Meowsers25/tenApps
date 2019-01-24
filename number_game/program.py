import random

print('---------------------------')
print('    GUESS THE NUMBER')
print('---------------------------')
print()

the_number = random.randint(0, 100)
# print(the_number)
guess = -1

name = input('What is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print(f'{guess} is TOO LOW')
    elif guess > the_number:
        print(f'{guess} is TOO HIGH')
    else:
        print(f'Excellent work {name}, YOU WIN!')

print('GAME OVER')
