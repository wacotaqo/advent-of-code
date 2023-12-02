# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque
from functools import reduce

filename = "adventofcode2022_day16_input.txt"
filename = "adventofcode2022_day16_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

valve_next = {}
valve_flow = {}
for line in lines:
    line = line.split()
    from_valve = line[1]
    valve_flow[from_valve] = int(line[4].split('=')[1][:-1])
    valve_next[from_valve] = [i.replace(',', '') for i in line[9:]]

def release_1_min(opened, released):
    for v in opened:
        released += valve_flow[v]
    return released

for v in valve_flow:
    print("%s = %s, %s" % (v, valve_flow[v], valve_next[v]))
print("Read %s valves" % len(valve_flow))
mins = 30
paths = deque([(0, 'AA', [], 30)])
max_released = 0
OPT_OPEN = 1
OPT_WALK = 2
OPT_NONE = 3

def get_action_name(action):
    return {OPT_OPEN: "Open", OPT_WALK: "Walk", OPT_NONE: "None"}[action]

def get_best_option(thisv, opened, timeleft, selectedv=None, go_depth=None):
    if not go_depth:
        go_depth = 5 # look a few steps ahead
    else:
        go_depth -=1
    if go_depth == 0 or timeleft < 1:
        return (-1, None, OPT_NONE)

    # Will try to find action with the best return in the time left
    # existing opened can be ignored as the past cannot be changed
    options = []

    #print("get_best_option for: %s %s %s, %s, %s" % (thisv, opened, timeleft, selectedv, go_depth))
    # Case: To open the current valve at a cost of 1 minute
    if not thisv in opened and valve_flow[thisv] > 0 and timeleft > 1:
        nextselectedv = selectedv if selectedv else thisv
        if thisv != nextselectedv:
            action = OPT_WALK
        else:
            action = OPT_OPEN
        options.append((valve_flow[thisv] * (max(0, timeleft-1)), nextselectedv, action))

    # Case: To follow the path to one of the next valves
    for nextv in valve_next[thisv]:
        nextselectedv = selectedv if selectedv else nextv
        # Check return for opening the next valve
        if not nextv in opened:
            options.append((valve_flow[nextv] * (max(0, timeleft-2)), nextselectedv, OPT_WALK))

        # Take 1 minute to go to another valve and get the best open for each of the next valves
        (er, v, o) = get_best_option(nextv, opened, timeleft-1, nextselectedv, go_depth)
        if o != OPT_NONE:
            options.append((er, v, o))

    if not options:
        return (-1, None, OPT_NONE)

    #print("Options: %s" % str(options))
    options.sort()
    # best option is now at the back of the list. This is what is should look like
    (expected_release, valve, option) = options[-1]
    #print("Best option: %s" % str(options[-1]))
    return (expected_release, valve, option)

print(paths)
timestep = 31
while paths:
    (released, thisv, opened, timeleft) = paths.popleft()

    if timeleft < 1:
        print((released, thisv, opened, timeleft))
        print(paths)
        break

    if timestep != timeleft:
        timestep = timeleft
        print("=============================")
        print("minute: %s" % timestep)
        print(paths)

    print("Timeleft(%s) - At %s - opened %s - release %s " % (timeleft, thisv, opened, released))
    (expected_release, valve, option) = get_best_option(thisv, opened, timeleft)
    print("Found best option: action %s on valve %s for return %s" % (get_action_name(option), valve, expected_release))
    if option == OPT_OPEN:
        assert not (valve in opened)
        paths.append((release_1_min(opened, released), valve, opened + [thisv], timeleft-1))
    elif option == OPT_WALK:
        paths.append((release_1_min(opened, released), valve, opened, timeleft-1))
    else: # OPT_NONE
        break

print("Done")
print(len(paths))