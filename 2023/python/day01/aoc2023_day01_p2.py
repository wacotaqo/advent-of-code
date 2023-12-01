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

replace = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9'), ('ten', '10')]

#debug("Input read: %s " % assignment_input)
debug("Input lines: %s" % len(assignment_input))

values = []

def process_input(input):
    for line in input: 
        #print(line)
        extracts = []
        for pos in range(0, len(line)):
            part = line[pos:]
            #print(part)
            if part[0].isdigit():
                extracts.append(part[0])
            else:
                for (replace_txt, replace_dig) in replace: 
                    if part[:len(replace_txt)] == replace_txt:
                        extracts.append(replace_dig)
                        break
            #print(extracts)
        extracts = [int(x) for x in extracts]
        if len(extracts) >0: 
            values.append(extracts[0]*10 + extracts[-1])
        #print(line, values[-1])
    total = sum(values)
    print("Total of %s lines = %s" % (len(input), total))

process_input(assignment_input)
