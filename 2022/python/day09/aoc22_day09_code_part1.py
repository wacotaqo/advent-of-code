# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os

filename = "adventofcode2022_day09_input.txt"
filename = "adventofcode2022_day09_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

print(assignment_input)