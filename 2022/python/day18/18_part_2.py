# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce, cache

filename = "18_input.txt"
filename = "18_input_test.txt"

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
part2 = []

(xs, ys, zs) = list(zip(*droplets))
minx = min(xs)
maxx = max(xs)
miny = min(ys)
maxy = max(ys)
minz = min(zs)
maxz = max(zs)

outside = set()
inside  = set()

@cache
def is_inside(x, y, z):
    blocked = 0
    for (cx, cy, cz) in checks:
        (tx, ty, tz) = (x, y, z)
        stop = False
        while not stop:
            tx += cx
            ty += cy
            tz += cz
            if minx<=tx<=maxx and miny<=ty<=maxy and minz<=tz<=maxz:
                if set([(tx, ty, tz)]) & droplets:
                    stop = True
                    blocked += 1
            else:
                stop = True
    return blocked == len(checks)

# Building outside spaces
queue = deque([(minx-1, miny-1, minz-1)])
been = set()
print("Space: %s-%s, %s-%s, %s-%s" % (minx, maxx, miny, maxy, minz, maxz))
while queue:
    # Check current location
    (x, y, z) = queue.popleft()
    #print("Check ", x, y, z)
    pos = set([(x, y, z)])
    if not(pos & droplets):
        outside.add((x, y, z))
    been.add((x, y, z))
    # check each direction
    for (cx, cy, cz) in checks:
        (nx, ny, nz) = (x+cx, y+cy, z+cz)
        pos = set([(nx, ny, nz)])
        if minx-1<=nx<=maxx+1 and miny-1<=ny<=maxy+1 and minz-1<=nz<=maxz+1 and not (pos & been) and not (nx, ny, nz) in queue:
            queue.append((nx, ny, nz))

print("Total volume if 3D rectangle with dropslets and 1 space out: %s x %s x %s = %s" % (maxx-minx+3, maxy-miny+3, maxz-minz+3, (maxx-minx+3)*(maxy-miny+3)*(maxz-minz+3)))
print("Number of droplets: %s" % len(droplets))
print("Number of outside spaces: %s" % len(outside))
outside_l = list(outside)
outside_l.sort()

@cache
def is_outside(x, y, z):
    pos = set([(x, y, z)])
    return len(pos & outside) == 1

for (x, y, z) in droplets:
    sides_free = 6
    sides_cooled = 6
    assert is_outside(x, y, z) == False
    for (cx, cy, cz) in checks:
        (tx, ty, tz) = (x+cx, y+cy, z+cz)
        pos = set([(x+cx, y+cy, z+cz)])
        if droplets & pos:
            sides_free -= 1
            sides_cooled -= 1
        else:
            o1 = is_inside(x+cx, y+cy, z+cz)
            o2 = is_outside(x+cx, y+cy, z+cz)
            if not o2:
                sides_cooled -= 1

    part1.append((x, y, z, sides_free))
    part2.append((x, y, z, sides_cooled))

total_free_sides = sum([d[3] for d in part1])
print("Part 1: Droplet of size %s has %s sides free." % (len(part1), total_free_sides))
total_cooled_sides = sum([d[3] for d in part2])
print("Part 2: Droplet of size %s has %s sides cooled." % (len(part1), total_cooled_sides))

