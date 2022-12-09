# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os

filename = "adventofcode2022_day09_input.txt"
#filename = "adventofcode2022_day09_input_test1.txt"
#filename = "adventofcode2022_day09_input_test2.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

DIR_R = (1, 0)
DIR_L = (-1, 0)
DIR_U = (0, 1)
DIR_D = (0, -1)

def sign(i):
    return (i>0) - (i<0)

def directionToFollow(pos1, pos2):
    x_dist = pos1[0] - pos2[0]
    y_dist = pos1[1] - pos2[1]
    distance = (x_dist ** 2 + y_dist ** 2) ** 0.5
    if distance >= 2:
        direction = (sign(x_dist), sign(y_dist))
        return direction
    else:
        return None

DIRECTIONS = {
    'R': DIR_R,
    'L': DIR_L,
    'U': DIR_U,
    'D': DIR_D
}

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

print(assignment_input)

start_location = (0, 0)
num_knots = 10
knots = range(0, num_knots)
knot_positions = {}
knot_locations = {}
for knot in knots:
    knot_positions[knot] = start_location   # current position of each knot
    knot_locations[knot] = [start_location] # history of location of each knot

# generate head_path
head_steps = []
for row in assignment_input:
    (direction, steps) = row.split(' ')
    head_steps.extend([*(int(steps)*direction)])

# Now traverse head in its path
move = 0
for step in head_steps:
    move += 1
    debug("Move %s: Head moves %s" % (move, step))
    for knot in knots:
        knot_pos = knot_positions[knot]
        if knot == 0:
            # Move the head in given direction
            direction = DIRECTIONS[step]
        else:
            # See if we move non-head knots
            direction = directionToFollow(knot_positions[knot-1], knot_pos)
        if direction:
            new_knot_pos = (knot_pos[0] + direction[0], knot_pos[1] + direction[1])
            knot_positions[knot] = new_knot_pos
            knot_locations[knot].append(new_knot_pos)
            debug("  knot[%s] moves %s from %s to %s" % (knot, direction, knot_pos, new_knot_pos))

debug("")
tail_locations = knot_locations[num_knots-1]
debug("Tail knot visits num locations: %s" % len(tail_locations))
# remove duplicates to get unique locations
tail_locations = [t for t in (set(tuple(i) for i in tail_locations))]
debug("number of unique tail locations: %s" % len(tail_locations))
#print(tail_locations)

