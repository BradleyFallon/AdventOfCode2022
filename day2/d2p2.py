# This time, XYZ means in lose draw win

ROCK = 1
PAPER = 2
SCISORS = 3

SYMBOLS = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISORS,
    'X': 0,
    'Y': 1,
    'Z': 2
}

# to win, +1. to lose, -1. to draw +-0.

p2_score = 0

with open('input.txt', 'r') as f:
    for line in f:
        p1_choose = SYMBOLS[line[0]]
        p2_outcome = SYMBOLS[line[2]]

        p2_choose = ( p2_outcome - 2 + p1_choose ) % 3 + 1
        p2 = 3*p2_outcome + p2_choose 

        p2_score += p2

print("p2_score: ", p2_score)

