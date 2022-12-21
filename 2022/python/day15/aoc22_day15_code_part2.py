# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2022_day15_input.txt"
#filename = "adventofcode2022_day15_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
lines = fh.read().splitlines()
fh.close()
print(lines)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

sensors = []
beacons = []
for line in lines:
    parts = [p1 for subline in line.split(':') for p1 in subline.split() if '=' in p1]
    parts = [int(p2[1].replace(',', '')) for p2 in [p1.split('=') for p1 in parts]]
    (sx, sy), (bx, by) = (parts[0], parts[1]), (parts[2], parts[3])
    sensors.append(((sx, sy), (bx, by), manhattan_distance(sx, sy, bx, by)))
    beacons.append((bx, by))

print("Number of sensors: %s" % len(sensors))
print("Number of beacons: %s" % len(beacons))

def possible_spot(cx, cy):
    if not(0<=cx<=4000000 and 0<=cy<=4000000):
        return False
    # Check it is not in range of any of the sensors
    for ((sx, sy), (bx, by), d) in sensors:
        if manhattan_distance(sx, sy, cx, cy) <= d:
            return False
    return True

# Check just outside each sensor:
for ((sx, sy), (bx, by), d) in sensors:
    #print("Point: %s" % str((sx, sy, d)))
    for (factorx, factory) in ((-1, -1), (1, -1), (1, 1), (-1, 1)):     # Check all diagonals
        #print("Direction: %s and distance: %s" % (str((signx, signy)), d+1))
        for i in range(d+2): # at distance d+1
            cx = sx + (factorx * (d+1-i))
            cy = sy + (factory * i)
            #print("From (%s, %s) dir (%s, %s) distance %s case %s: %s, %s" % (sx, sy, signx, signy, d+1, i, cx, cy))
            if possible_spot(cx, cy):
                print("Found the spot!: %s, %s" % (cx, cy))
                print("Frequency: %s" % (cx*4000000+cy))
