# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os

filename = "adventofcode2022_day09_input.txt"
#filename = "adventofcode2022_day09_input_test1.txt"

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

#def directionToFollow(pos1, pos2):
#    x_dist = pos1[0] - pos2[0]

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
head = tail = start_location
head_locations = [head] # not needed, but track for fun
tail_locations = [tail]

# generate head_path
head_steps = []
for row in assignment_input:
    (direction, steps) = row.split(' ')
    head_steps.extend([*(int(steps)*direction)])

# Now traverse head in its path
move = 0
for step in head_steps:
    move += 1
    print("Move %s - head%s tail%s" % (step, head, tail))
    # Move the head
    direction = DIRECTIONS[step]
    head = (head[0] + direction[0], head[1] + direction[1])
    head_locations.append(head)

    print("  head moves %s to %s" % (step, head_locations[-1]))

    # See if we move the tail
    x_dist = head[0]-tail[0]
    y_dist = head[1]-tail[1]
    distance = (x_dist**2 + y_dist**2)**0.5
    print("  tail is distance(dx:%s, dy:%s, d:%s)" % (x_dist, y_dist, distance))
    if distance >= 2:
        tail_direction = (sign(x_dist), sign(y_dist))
        tail = (tail[0] + tail_direction[0], tail[1] + tail_direction[1])
        tail_locations.append(tail)
        print("    so tail moves %s to %s" % (tail_direction, tail))

print("number of head locations: %s" % len(head_locations))
print("number of tail locations: %s" % len(tail_locations))
#print(tail_locations)
# remove duplicates to get unique locations
tail_locations = [t for t in (set(tuple(i) for i in tail_locations))]
print("number of unique tail locations: %s" % len(tail_locations))
#print(tail_locations)

