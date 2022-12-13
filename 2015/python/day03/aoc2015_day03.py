import os

filename = "aoc2015_day03_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
input = fh.read().splitlines()
fh.close()

print(input)

x = 0
y = 0
houses = {(x, y): 1}
directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
for move in input[0]:
    (dx, dy) = directions[move]
    (x, y) = (x+dx, y+dy)
    if not((x, y) in houses):
        houses[(x, y)] = 1
    else:
        houses[(x, y)] += 1
print("Houses delivered presents: %s" % len(houses.keys()))
