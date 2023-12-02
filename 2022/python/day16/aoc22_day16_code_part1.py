# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2022_day16_input.txt"
#filename = "adventofcode2022_day16_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

valves = {}
for line in lines:
    line = line.split()
    #print(line)
    from_valve = line[1]
    flow_rate = int(line[4].split('=')[1][:-1])
    to_valves = [i.replace(',', '') for i in line[9:]]
    valves[from_valve] = (flow_rate, to_valves)

def release_1_min(opened, released):
    for v in opened:
        released += valves[v][0]
    return released

for v in valves:
    print("%s = %s" % (v, valves[v]))
print("Read %s valves" % len(valves))
mins = 30
paths = deque([(0, 'AA', [], 30)])
r = 0
max_released = 0
max_opened = 0
while r < 1000000:
    r += 1

    (released, valve, opened, minute) = paths.popleft()
    (flow_rate, to_valves) = valves[valve]
    if released > max_released:
        max_released = released
    if max_opened < len(opened):
        max_opened = len(opened)

    if minute != mins:
        print("New minute: %s %s %s %s, %s" % (minute, released, len(paths), opened, valve))
        mins = minute

    if minute < 0:
        break # times up

    #if max_released > 100:
    #    if ((released < (max_released * 0.85)) or (len(opened) < (max_opened - 2))):
            # if too far behind, skip these cases
    #        continue

    # case: open an unopened valve
    if flow_rate > 0 and not(valve in opened):
        new_release = release_1_min(opened, released)
        new_scenario = (released, valve, opened + [valve], minute-1)
        if not new_scenario in paths:
            paths.append(new_scenario)
    else:
        # case: take one of the tunnels
        for v in to_valves:
            new_scenario = (release_1_min(opened, released), v, opened, minute-1)
            if not new_scenario in paths:
                paths.append(new_scenario)

#paths = list(paths)
#paths.sort()

paths = list(paths)
print(len(paths))
print(paths[:20])
print("Max released: %s" % max_released)