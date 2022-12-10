# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os

filename = "adventofcode2022_day10_input.txt"
#filename = "adventofcode2022_day10_input_test1.txt"
#filename = "adventofcode2022_day10_input_test2.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

debug("Input read: %s " % assignment_input)

cycle = 0
register_x = 1 # Start as 1
report_at_cycle = 20

crt = []
crt_row = ''
crt_x = 0

def next_cycle(prefix2):
    global cycle
    global crt
    global crt_row
    global crt_x
    cycle += 1

    if crt_x >= register_x-1 and crt_x <= register_x+1:
        crt_row += '#'
    else:
        crt_row += '.'

    crt_x += 1 # next pixel
    if crt_x % 40 == 0:   # when at end of row
        crt.append(crt_row) # store row
        crt_row = ''        # and cycle to a new row
        crt_x = 0

def process_input(input):
    for instruction in input:
        global processing_queue
        global register_x
        global report_at_cycle

        next_cycle("Start")

        debug("%5s: Processing instruction(%12s) x(%25s)" % (cycle, instruction, register_x))
        if instruction == 'noop':
            pass
        else: # expecting "addx <num>"
            next_cycle("During") # needs an additional cycle
            value = instruction.split(' ')[1]
            register_x += int(value)
            debug("%30s%12s  ==> Adding value(%s) and extra 1 cycle" % ('', instruction, value))


process_input(assignment_input)
debug("")
print("Register X: %s" % register_x)

for row in crt:
    print(row)
