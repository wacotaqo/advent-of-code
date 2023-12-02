# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2021_day24_input.txt"
#filename = "adventofcode2021_day24_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()
#lines = ["inp x", "mul x -1"]
#print(lines)

"""
auto_input = '99999999999999'
def get_input(txt):
    global auto_input
    #return input(txt)
    if auto_input:
        input = auto_input[0]
        auto_input = auto_input[1:]
        return input
    else:
        return ''
"""

regs = {'z': 0, 'w': 0, 'y': 0, 'x': 0}
auto_input = ''
def attribeval(attrib):
    if attrib.isnumeric():
        return int(attrib)
    elif attrib[0] == '-' and attrib[1:].isnumeric():
        return int(attrib)
    elif attrib in regs:
        return regs[attrib]
    else:
        print("Cannot evaluate attrib %s" % attrib)
        assert False

def run_ALU_with_input(auto_input):

    def get_input(txt):
        global auto_input
        if auto_input:
            input = auto_input[0]
            auto_input = auto_input[1:]
            return input
        else:
            return '0'

    for line in lines:
        parts = line.split()
        command = parts[0]
        attr1 = parts[1]
        if len(parts) > 2:
            attr2 = parts[2]
        else:
            attr2 = None

        if command == 'inp':
            inp = get_input("Provide variable %s: " % attr1)
            regs[attr1] = int(inp)
        elif command == 'add':
            regs[attr1] = regs[attr1] + attribeval(attr2)
        elif command == 'mul':
            regs[attr1] = regs[attr1] * attribeval(attr2)
        elif command == 'mod':
            regs[attr1] = regs[attr1] % attribeval(attr2)
        elif command == 'div':
            regs[attr1] = regs[attr1] // attribeval(attr2)
        elif command == 'eql':
            regs[attr1] = 1 if regs[attr1] == attribeval(attr2) else 0
        else:
            print("Unknown command: %s" % (parts))

def valid(num):
    numstr = str(num)
    return not ('0' in numstr)

a = 11999119991199
while a >= 11111111111111:
    regs = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    if a % 999 == 0:
        print("a = %s" % a)
        print("regs: %s" % str(regs))
    run_ALU_with_input(str(a))
    if a % 999 == 0:
        print("regs: %s" % str(regs))
    a = a-1
    while not valid(a):
        a = a-1

reg_names = list(regs.keys())
reg_names.sort()
for reg_name in reg_names:
    print("%s = %s" % (reg_name, regs[reg_name]))

if len(auto_input) > 0:
    print("Unused input: %s" % auto_input)