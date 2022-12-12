# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os

filename = "adventofcode2022_day12_input.txt"
#filename = "adventofcode2022_day12_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

def print_map(mymap):
    maxR = len(mymap)
    print("Map (%s, %s)" % (len(mymap[0]), maxR))
    for r in range(maxR):
        print(''.join([' %3s ' % c for c in mymap[r]]))

TOPO = {(99, 99): "#####", (-1, -1): "((S))", (26, 26): "((X))", (0,5): '  .  ', (6,10): '  o  ', (11, 15): 'O', (16, 20): '¢', (21,23): '0', (24,24): '$', (25,25):'@'}
def get_topo(c):
    topo = '.'
    if c > 13 and c < 26:
        topo = chr(c+97)
    else:
        for (low, high) in TOPO.keys():
            if c >= low and c <= high:
                topo = TOPO[(low,high)]
                break
    return '%5s'%topo

def print_path(path, mymap):
    print(path)
    maxR = len(mymap)
    maxC = len(mymap[0])
    pathmap = [[get_topo(mymap[r][c]) for c in range(maxC)] for r in range(maxR)]
    step = 1
    last = path[-1]
    for (col, row) in path:
        if (col, row) == last:
            pathmap[row][col] = '(%3s)' % step
        else:
            pathmap[row][col] = '%3s%s ' % (step, chr(mymap[row][col]+97))
        step += 1
    print("Showing path: len(%s) last 5 points (%s)" % (len(path), path[-5:]))
    print_map(pathmap)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read()
fh.close()

mymap = []
r = 0
start = ()
end = ()
lowestC = ord('a')
SC = ord('S')-lowestC
EC = ord('E')-lowestC
wallC = 99
debug_from_step = 500
for _ in assignment_input.split('\n'):
    cols = list(map(lambda x: ord(x)-lowestC, list(_)))
    cols = [wallC] + cols + [wallC]
    if SC in cols:
        start = (cols.index(SC), r+1)
        cols[start[0]] = -1
    if EC in cols:
        end = (cols.index(EC), r+1)
        cols[end[0]] = 26
    mymap.append(cols)
    r += 1
maxR = len(mymap)
maxC = len(mymap[0])
mymap = [[wallC]*maxC] + mymap + [[wallC]*maxC]

print(assignment_input)
print()
print_map(mymap)
print()
print("Map(%s, %s)"% (maxR, maxC))
print("Start(%s) --> End(%s)" % (start, end))

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
paths = [[start]]
already_been = [start]
path_found = []
for step in range(1000):
    if step == 0 or step > debug_from_step:
        print("Round %s: paths(%s)" % (step, len(paths)))
    new_paths = []
    for path in paths: # Try each path
        pos = path[-1]
        height = mymap[pos[1]][pos[0]]
        if step == 0 or step > debug_from_step:
            print("  %s: pos(%s) h(%s) path(%s)" % (len(path), pos, height, path))
        possible_directions = []
        posc = chr(mymap[pos[1]][pos[0]]+97)
        for d in DIRS:
            newpos = (pos[0]+d[0],pos[1]+d[1])
            newposc = chr(mymap[newpos[1]][newpos[0]] + 97)
            if step > debug_from_step:
                print(newpos)
            newposheight = mymap[newpos[1]][newpos[0]]
            if step > debug_from_step:
                print("     dir(%s) newpos(%s) newh(%s) h(%s)" % (d, newpos, newposheight, height))
            if newpos in already_been: # or go to a a place I have already been (inefficient)
                if step > debug_from_step:
                    print("       already been. stop this path.")
                continue
            elif newposheight - height > 1:
                if step > debug_from_step:
                    print("       step too big. stop this path.")
                continue
            elif newposheight == 26:
                path.append(newpos)
                path_found = path
            else:
                possible_directions.append((newposheight, newpos))
        if path_found:
            break
        if len(possible_directions) > 0:
            for possible_direction in possible_directions:
                if step > debug_from_step:
                    print("    Adding path: %s" % str(possible_direction))
                new_paths.append(path + [possible_direction[1]])
        if path_found:
            break
    if path_found:
        break

    if len(new_paths) == 0 and not path_found:
        # We should never be here
        print("No more paths, yet we have not reached the summit. Something is wrong!")
        print("Step: %s" % step)
        print("Paths: %s (%s" % (len(paths), [len(p) for p in paths]))
        print_map(mymap)
        for p in paths:
            print_path(p, mymap)
        break

    paths = new_paths

    # Remove alternative paths that lead to the same place in the same number of steps
    one_path_per_distance_for_each_position = {}
    for p in paths:
        pos = p[-1]
        l = len(p)
        if not (pos, l) in one_path_per_distance_for_each_position:
            one_path_per_distance_for_each_position[(pos, l)] = p
    paths = list(one_path_per_distance_for_each_position.values())

    # remember where these paths have led us
    already_been = [pos for path in paths for pos in path]
    already_been = list(set(already_been))
    already_been.sort()


if path_found:
    print("At the highest point!")
    print("After %s steps." % (len(path_found)-1))
    print(path_found)
    print_path(path_found, mymap)
