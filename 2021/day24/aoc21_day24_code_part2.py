# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2021_day24_input.txt"
filename = "adventofcode2021_day24_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

print(lines)