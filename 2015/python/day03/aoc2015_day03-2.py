import os

filename = "aoc2015_day03_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
input = fh.read().splitlines()
fh.close()

print(input)

givers = [(0, 0), (0, 0)]
houses = {(0, 0): 2}
directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
next_giver = 0
for move in input[0]:
    (dx, dy) = directions[move]
    (x, y) = givers[next_giver]
    (nx, ny) = (x+dx, y+dy)
    if not((nx, ny) in houses):
        houses[(nx, ny)] = 1
    else:
        houses[(nx, ny)] += 1
    givers[next_giver] = (nx, ny)
    next_giver = (next_giver + 1) % 2

print("Houses delivered presents: %s" % len(houses.keys()))
