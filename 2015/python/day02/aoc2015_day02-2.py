import os

filename = "aoc2015_day02_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
input = fh.read().splitlines()
fh.close()

print(input)
