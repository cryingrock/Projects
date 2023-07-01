import random

choice = ['rock', 'paper', 'scissors']
while True:
    game = input('Do you want play Y or N: ')
    if game == 'Y':
        p1 = input('choose a number 0 - rock, 1 - paper, 2 - scissors: ')
        p1 = choice[int(p1)]
        p2 = choice[random.randint(0, 3)]
        if p1 == p2:
            print('Draw', p1, p2)
        elif p1 == 'rock' and p2 == 'paper' or p1 == 'paper' and p2 == 'scissors' or p1 == 'scissors' and p2 == 'rock':
            print('Computer won', p1, p2)
        else:
            print('Player won', p1, p2)
    elif game=='N':
        print('Goodbye')
        break
