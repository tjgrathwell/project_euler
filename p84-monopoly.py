# The other way to solve this problem is markov chain: make a table of probabilities to get from each state to each other state, do some magic with eigenvalues, dance dance

board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

import random
from collections import defaultdict

def get_next(position, type):
    for spot in board[position:] + board[:position]:
        if spot.startswith(type):
            result = spot
            return board.index(result)

def play(position):
    # move the position around on board according to arcane rules
    finished = False
    while not finished:
        finished = True
        place = board[position]
        if place.startswith('G2J'):
            position = board.index('JAIL')
        elif place.startswith('CC'):
            card = random.randint(1,16)
            if card == 1:
                position = board.index('GO')
            elif card == 2:
                position = board.index('JAIL')
        elif place.startswith('CH'):
            card = random.randint(1,16)
            if card == 1:
                position = board.index('GO')
            elif card == 2:
                position = board.index('JAIL')
            elif card == 3:
                position = board.index('C1')
            elif card == 4:
                position = board.index('E3')
            elif card == 5:
                position = board.index('H2')
            elif card == 6:
                position = board.index('R1')
            elif card in [7,8]:
                position = get_next(position, 'R')
            elif card == 9:
                position = get_next(position, 'U')
            elif card == 10:
                position -= 3
                finished = False
    return position
            
dice_sides, dice_num = 4, 2
position = 0
rolls = 2000000
landed = defaultdict(int)
consecutive_doubles = 0
for i in xrange(rolls):
    rolls = [random.randint(1,dice_sides) for die in xrange(dice_num)]
    if rolls[0] == rolls[1]:
        consecutive_doubles += 1
    else:
        consecutive_doubles = 0
    if consecutive_doubles >= 3:
        position = board.index('JAIL')
    else:
        roll = sum(rolls)
        position = play((position + roll) % 40)
    landed[position] += 1
    
reverso = dict([(v,k) for k,v in zip(landed.keys(), landed.values())])
for rolled in sorted(reverso):
    print rolled, reverso[rolled], board[reverso[rolled]]