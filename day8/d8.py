

vis_trees = set()

rows = list()
columns = list()


class Grid:
    def __init__(self, rows):
        self.rows = rows
        self.w = len(rows[0])
        self.h = len(rows)
    
    def get(self, x, y):
        x = x % self.w
        y = y % self.h
        return self.rows[y][x]


with open('input.txt', 'r') as f:
    for line in f:
        row = list()
        for number in line:
            try:
                row.append(int(number))
            except:
                pass
        rows.append(row)

grid = Grid(rows)


# count from left to right
for y in range(grid.h):
    tallest = -1
    for x in range(grid.w):
        height = grid.get(x, y)
        if height > tallest:
            tallest = height
            vis_trees.add((x, y))
        if height == 9:
            break

# count from right to left
for y in range(grid.h):
    tallest = -1
    for x in reversed(range(grid.w)):
        height = grid.get(x, y)
        if height > tallest:
            tallest = height
            vis_trees.add((x, y))
        if height == 9:
            break

# count from top to bottom
for x in range(grid.w):
    tallest = -1
    for y in range(grid.h):
        height = grid.get(x, y)
        if height > tallest:
            tallest = height
            vis_trees.add((x, y))
        if height == 9:
            break

# count from bottom to top
for x in range(grid.w):
    tallest = -1
    for y in reversed(range(grid.h)):
        height = grid.get(x, y)
        if height > tallest:
            tallest = height
            vis_trees.add((x, y))
        if height == 9:
            break

print(len(vis_trees))
        
