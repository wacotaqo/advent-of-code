import os

filename = "aoc2015_day0x_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()
