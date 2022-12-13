import os

filename = "aoc2015_day02_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
input = fh.read().splitlines()
fh.close()

print(input)

total_needed = 0
for row in input:
    (l, w, h) = [int(n) for n in row.split('x')]
    area_needed = 2*l*w + 2*w*h + 2*l*h + min([l*w, w*h, l*h])
    total_needed += area_needed

print(total_needed)