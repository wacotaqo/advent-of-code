# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "18_input.txt"
#filename = "18_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()
droplets = set([tuple(map(int, d.split(','))) for d in lines])
print(droplets)

checks = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))

part1 = []

for (x, y, z) in droplets:
    sides_free = 6
    for (cx, cy, cz) in checks:
        pos = set([(x+cx, y+cy, z+cz)])
        if droplets & pos:
            sides_free -= 1

    part1.append((x, y, z, sides_free))

total_free_sides = sum([d[3] for d in part1])
print("Droplet of size %s has %s sides free." % (len(part1), total_free_sides))

