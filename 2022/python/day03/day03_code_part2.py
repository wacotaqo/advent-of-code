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

num_rucksacks_checked = 0
groups_found = 0
group_size = 3
sum_priorities = 0
num_rucksacks = len(elves_rucksacks)
num_groups = num_rucksacks / 3

if not num_groups.is_integer():
    print("We have an unexpected number of rucksacks and groups. %s - %s" % (num_rucksacks, num_groups))
    exit()

for group_first_racksack in range(0, num_rucksacks, 3):
    groups_found += 1
    group_rucksacks = elves_rucksacks[group_first_racksack:group_first_racksack+3]
    print("%d: Group racksacks: %s" % (groups_found, group_rucksacks))

    (rucksack1, rucksack2, rucksack3) = group_rucksacks
    group_badge = 0
    for item in rucksack1:
        has_duplicates = (rucksack2.find(item) > -1) and (rucksack3.find(item) > -1)
        if has_duplicates:
            group_badge = item
            break

    if group_badge:
        group_priority = get_priority(group_badge)
        sum_priorities += group_priority

        print("%d: Group badge = %s, prio = %d" %(groups_found, group_badge, group_priority))

print("Sum of all group priorities: %s" % sum_priorities)