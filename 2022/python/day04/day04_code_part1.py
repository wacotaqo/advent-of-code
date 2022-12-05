# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re

filename = "adventofcode2022_day04_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

assignment_regex = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

overlapping_assignments = []
for one_assignment in assignment_input:
    ro = re.match(assignment_regex, one_assignment)
    if ro:
        (elf1_start, elf1_end, elf2_start, elf2_end) = [eval(i) for i in ro.groups()]
        if (((elf1_start <= elf2_start) and (elf1_end >= elf2_end))
            or ((elf2_start <= elf1_start) and (elf2_end >= elf1_end))):
            overlapping_assignments.append(((elf1_start, elf1_end, elf2_start, elf2_end), one_assignment))
    else:
        print("no match: %s" % assignment_input)
        continue

for oa in overlapping_assignments:
    print(oa)
print("Overlapping assignments: %s" % len(overlapping_assignments))
