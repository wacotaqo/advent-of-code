# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
from collections import Counter

filename = "adventofcode2022_day06_input.txt"
#filename = "adventofcode2022_day06_input_test.txt"

def duplicates(l):
    dups = Counter(l) - Counter(set(l))
    return list(dups.keys())

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read()
fh.close()

print("Input: %s" % assignment_input)

start_of_packet_marker = ''
chars_read = 0

for i in range(0, len(assignment_input)-4):
    letters4 = assignment_input[i:i+4]
    dups = duplicates(letters4)
    if not(dups):
        start_of_packet_marker = letters4
        chars_read = i+4
        break

if chars_read > 0:
    print("Found Start-of-packet-marker (%s) after %d characters." % (start_of_packet_marker, chars_read))
else:
    print("No marker found.")