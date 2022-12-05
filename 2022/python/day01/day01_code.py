import os
import sys

filename = "adventofcode2022_day01_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
calories_input = fh.read().splitlines()
fh.close()

elf_count = 0
elf = ()
elves = {}
calories_input.append("")
for calories in calories_input:
    if calories.isnumeric():
        icalories = int(calories)
        if elf:
            elf[0] = elf[0]+1
            elf[1] += icalories
            elf[2].append(icalories)
        else:
            elf = [1, icalories, [icalories]]
    else:
        elf_count += 1
        elves[elf_count] = elf
        # print("New elf %d = %s" % (elf_count, elf))
        elf = ()
        
list_of_calories  = [calories for (num, calories, items) in elves.values()]
list_of_calories.sort()

print("method 1: The most calories carried = %d" % max(calories for (num, calories, items) in elves.values()))
print("method 2: The most calories carried = %d" % list_of_calories[-1])

print("Sum of calories held by the 3 elves with the most calories (%s) = %s" % (list_of_calories[-3:], sum(list_of_calories[-3:])))


    

