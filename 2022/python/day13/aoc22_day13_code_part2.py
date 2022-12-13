# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce, cmp_to_key

filename = "adventofcode2022_day13_input.txt"
#filename = "adventofcode2022_day13_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
input = fh.read().strip()
fh.close()
input = [eval(row) for row in input.split('\n') if not row == '']

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

compare_to_key = cmp_to_key(compare)

divider1 = [[2]]
divider2 = [[6]]
input.append(divider1)
input.append(divider2)

input.sort(key=compare_to_key)

for i in input:
    print(i)

decoder_key = 1
for i in range(len(input)):
    if input[i] == divider1 or input[i] == divider2:
        decoder_key *= i+1
print("Decoder key = %s" % decoder_key)