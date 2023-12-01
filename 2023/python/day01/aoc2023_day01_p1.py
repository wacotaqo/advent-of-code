# This program is an exercise/challenge from the 2023 advent of code competition
#
#
import os
import re

filename = "adventofcode2023_day01_input.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

#debug("Input read: %s " % assignment_input)
debug("Input lines: %s" % len(assignment_input))

values = []

def process_input(input):
    for line in input: 
        extracts = [int(x) for x in list(filter(lambda x: x.isdigit(), list(line)))]
        if len(extracts) >0: 
            values.append(extracts[0]*10 + extracts[-1])
        print(line, values[-1])
    total = sum(values)
    print("Total of %s lines = %s" % (len(input), total))

process_input(assignment_input)
