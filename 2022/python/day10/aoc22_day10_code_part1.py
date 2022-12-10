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
signal_strengths = []

def process_input(input):
    for instruction in input:
        global cycle
        global processing_queue
        global register_x
        global report_at_cycle

        cycle += 1
        if cycle == report_at_cycle:
            ss = register_x * cycle
            debug("%7sReporting signal strength: %s x %s = %s" % ('', cycle, register_x, ss))
            signal_strengths.append(ss)
            report_at_cycle += 40

        debug("%5s: Processing instruction(%12s) x(%25s)" % (cycle, instruction, register_x))
        if instruction == 'noop':
            pass
        else: # expecting "addx <num>"
            cycle += 1 # needs an additional cycle
            if cycle == report_at_cycle:
                ss = register_x * cycle
                debug("%7sReporting signal strength: %s x %s = %s" % ('', cycle, register_x, ss))
                signal_strengths.append(ss)
                report_at_cycle += 40

            value = instruction.split(' ')[1]
            register_x += int(value)
            debug("%30s%12s  ==> Adding value(%s) and extra 1 cycle" % ('', instruction, value))


process_input(assignment_input)
debug("")
print("Register X: %s" % register_x)
print("Sum of %s signal strengths: %s" % (len(signal_strengths), sum(signal_strengths)))