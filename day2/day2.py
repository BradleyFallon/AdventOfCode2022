

ROCK = 1
PAPER = 2
SCISORS = 3

SYMBOLS = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISORS,
    'A': ROCK,
    'B': PAPER,
    'C': SCISORS
}

p1_score = 0
p2_score = 0

with open('input.txt', 'r') as f:
    for line in f:
        p1 = SYMBOLS[line[0]]
        p2 = SYMBOLS[line[2]]
        diff = p1 - p2    
        if diff == 0:
            # tie
            p1 += 3
            p2 += 3
        elif diff%3 == 2 :
            # p1 loses  1-2=-1 pbr  2-3=-1 sbp 3-1=2 rbs
            p2 += 6
        else:
            p1 += 6

        p1_score += p1
        p2_score += p2
        p1 = 0; p2 = 0

print("p1_score: ", p1_score)
print("p2_score: ", p2_score)

