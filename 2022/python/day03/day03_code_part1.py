# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import sys

def get_priority(item):
    ascii_code = ord(item)
    if ascii_code >= 97 and ascii_code <= 122:
        return ascii_code-96 # 1..26
    if ascii_code >= 65 and ascii_code <= 90:
        return ascii_code-38 # 27..52
    return 0

filename = "adventofcode2022_day03_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
elves_rucksacks = fh.read().splitlines()
fh.close()

"""
# Test case:
elves_rucksacks = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''.splitlines()
"""

work_done = 0
sum_priorities = 0
duplicates_found = 0
for rucksack in elves_rucksacks:
    if len(rucksack) > 1:
        work_done += 1
        num_items = len(rucksack)
        num_compartment_items = int(num_items/2)
        left_compartment = rucksack[0:num_compartment_items]
        right_compartment = rucksack[num_compartment_items:]

        if rucksack != "%s%s" % (left_compartment, right_compartment):
            print("No match: %s = %s + %s" % (rucksack, left_compartment, right_compartment))

        duplicate_index = -1
        has_duplicate = False
        for item in left_compartment:
            duplicate_index = right_compartment.find(item)
            has_duplicate = duplicate_index >= 0
            if has_duplicate:
                duplicate_item = item
                print("%d: Row(%s) item %s in %s is also in %s" % (work_done, rucksack, item, left_compartment, right_compartment, ))
                break

        if has_duplicate:
            duplicates_found += 1
            print("%d: Duplicate item %s has priority %s" % (work_done, item, get_priority(item)))
            sum_priorities += get_priority(item)
        else:
            print ("no duplicates found: %s - %s" %(left_compartment, right_compartment))
    else:
        print("Unexpected content: %s" % rucksack)

print("After %s rucksacks and %s duplicates, total priorities is %s" % (work_done, duplicates_found, sum_priorities))
