

vis_trees = set()

rows = list()
columns = list()


class Grid:
    def __init__(self, rows):
        self.rows = rows
        self.w = len(rows[0])
        self.h = len(rows)
        self.x = 0
        self.y = 0
    
    def get(self, x, y):
        if x < 0 or y < 0:
            raise IndexError
        return self.rows[y][x]

    def _d_next(self, x, y, counter):
        self.x = x
        self.y = y
        this_h = self.get(self.x, self.y); print(this_h, "<-- this")
        d = 0
        next_h = -1
        while next_h < this_h:
            counter(self)
            try:
                next_h = self.get(self.x, self.y)
            except IndexError:
                print("EDGE")
                break
            d += 1
            print(next_h, d)

        print(next_h)
            
        print("RETURN: ", d)
        return d


    def d_next_r(self, x, y):
        print("RIGHT")
        def counter(grid): grid.x += 1
        return self._d_next(x, y, counter)

    def d_next_l(self, x, y):
        print("LEFT")
        def counter(grid): grid.x -= 1
        return self._d_next(x, y, counter)

    def d_next_u(self, x, y):
        print("UP")
        def counter(grid): grid.y += 1
        return self._d_next(x, y, counter)

    def d_next_d(self, x, y):
        print("DOWN")
        def counter(grid): grid.y -= 1
        return self._d_next(x, y, counter)


    def scenic_score(self, x, y):
        print("X, Y: ", x, ", ", y)
        r = self.d_next_r(x, y)
        l = self.d_next_l(x, y)
        u = self.d_next_u(x, y)
        d = self.d_next_d(x, y)
        scenic = r * l * u * d
        print("scenic: ", scenic)
        return scenic


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


scenic_max = 0
for y in range(grid.h):
    for x in range(grid.w):
        scenic = grid.scenic_score(x, y)
        if scenic > scenic_max:
            scenic_max = scenic


print("scenic_max: ", scenic_max)