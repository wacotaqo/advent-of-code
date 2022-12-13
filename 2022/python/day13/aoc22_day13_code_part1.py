# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2022_day13_input.txt"
#filename = "adventofcode2022_day13_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
input = fh.read().strip()
fh.close()
input = [pairs.split('\n') for pairs in input.split('\n\n')]

def compare(left, right):
    # < : -1 / > : 1 / == : 0
    #print("Comparing: %s ? %s" % (left, right))
    left = deque(left)
    right = deque(right)

    while left:
        x = left.popleft()
        if right:
            y = right.popleft()
        else:
            return 1

        if type(x) == type(1) and type(x) == type(y):
            if x < y:
                return -1
            if x > y:
                return 1
        elif type(x) == type([]) and type(x) == type(y):
            result = compare(x, y)
            if result in [1, -1]:
                return result
        elif type(x) == type(1) and type(y) == type([]):
            result = compare([x], y)
            if result in [1, -1]:
                return result
        elif type(x) == type([]) and type(y) == type(1):
            result = compare(x, [y])
            if result in [1, -1]:
                return result

    if right:
        return -1

    return 0

print(input)
sum_indices = 0
for index in range(len(input)):
    left, right = input[index]
    c = compare(eval(left), eval(right))
    if c == -1:
        sum_indices += index+1
print("After %s pairs, sum right indices = %s" % (len(input), sum_indices))
