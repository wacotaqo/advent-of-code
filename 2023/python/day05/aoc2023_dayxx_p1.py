# This program is an exercise/challenge from the 2023 advent of code competition
#
#
import os
import re

filename = "adventofcode2023_dayxx_input.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

debug("Input read: %s " % assignment_input)
debug("Input lines: %s" % len(assignment_input))

values = []

def process_input(input):
    print("process_input_done")
    
process_input(assignment_input)
print("result: %s" % values)