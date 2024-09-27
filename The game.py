import random

computer_move = ''
rock = 'rock'
paper = 'paper'
scissors = 'scissors'

player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid input try again')

computer_number_random = random.randint(1,3)

computer_move = computer_number_random

if computer_move == 1:
    computer_move = rock
elif computer_move == 2:
    computer_move = paper
elif computer_move == 3:
    computer_move = scissors

print(f'The computer chose {computer_move}')

if player_move == computer_move:
    print(f"It's a tie!")
elif (player_move == rock and computer_move == scissors) or (player_move == scissors and computer_move == paper) or \
    (player_move == paper and computer_move == rock):
    print(f'You Win')
else:
    print('You lose')


