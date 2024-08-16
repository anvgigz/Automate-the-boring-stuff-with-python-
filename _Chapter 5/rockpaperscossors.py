import random, sys

print('Rock, Paper, Scossors')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses. %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playermove = input()
        if playermove == 'q':
            sys.exit()
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break
    print('type one of r, p, s, or q')


    if playermove == 'r':
        print('rock versus...')
    elif playermove == 'p':
        print('paper versus...')
    elif playermove == 's':
        print('scissors versus...')

    randomnumber = random.randint(1,3)
    if randomnumber == 1:
        computermove = 'r'
        print('Rock')
    elif randomnumber == 2:
        computermove = 'p'
        print('Paper')
    elif randomnumber == 3:
        computermove = 's'
        print('Scissors')
    
    if playermove == computermove:
        print('Its a Tie')
        ties = ties + 1
    elif playermove == 'r' and computermove == 's':
        print('Player wins')
        wins = wins + 1
    elif playermove =='r' and computermove == 'p':
        print('Computer wins')
        losses = losses + 1
    elif playermove == 'p' and computermove == 'r':
        print('Player wins')
        wins = wins + 1
    elif playermove == 'p' and computermove == 's':
        print('computer wins')
        losses = losses + 1
    elif playermove == 's' and computermove == 'p':
        print('Player wins')
        wins = wins + 1
    elif playermove == 's' and computermove == 'r':
        print('computer wins')
        losses = losses + 1
