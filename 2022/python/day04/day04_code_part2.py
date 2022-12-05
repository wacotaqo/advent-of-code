# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re

filename = "adventofcode2022_day04_input.txt"

assignment_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()


assignment_regex = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

wholly_overlapping_assignments = []
overlapping_assignments = []
for one_assignment in assignment_input:
    ro = re.match(assignment_regex, one_assignment)
    if ro:
        (elf1_start, elf1_end, elf2_start, elf2_end) = [eval(i) for i in ro.groups()]
        if (((elf1_start <= elf2_start) and (elf1_end >= elf2_end))
            or ((elf2_start <= elf1_start) and (elf2_end >= elf1_end))):
            wholly_overlapping_assignments.append(((elf1_start, elf1_end, elf2_start, elf2_end), one_assignment))
        if (
            ((elf1_start <= elf2_start) and (elf1_end >= elf2_start))
            or ((elf1_start <= elf2_end) and (elf1_start >= elf2_start))
            or ((elf2_start <= elf1_start) and (elf2_end >= elf1_start))
            or ((elf2_start <= elf1_end) and (elf2_end >= elf1_end))
            ): # or the same as not((elf1_end < elf2_start) or (elf2_end < elf1_start))
            overlapping_assignments.append(((elf1_start, elf1_end, elf2_start, elf2_end), one_assignment))
    else:
        print("no match: %s" % assignment_input)
        continue

print("Wholly Overlapping assignments: %s" % len(wholly_overlapping_assignments))

for oa in overlapping_assignments:
    print(oa)
print("Overlapping assignments: %s" % len(overlapping_assignments))
