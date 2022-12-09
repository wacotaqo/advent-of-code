# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import functools

filename = "adventofcode2022_day08_input.txt"
#filename = "adventofcode2022_day08_input_test.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

DEBUG = 0
def debug(msg):
    if DEBUG:
        print(msg)

def isVisible(trees):
    debug("check visibility for trees in dir %s)" % str(trees))
    treeHeight = trees[0]
    check = [t for t in trees[1:] if t < treeHeight]
    if trees[1:] == []:
        return True # At the edge
    elif len(check) == len(trees)-1:
        return True # can see all the way
    else:
        return False

gridEastWest = {}
gridNorthSouth = {}
y = 0
for row in assignment_input:
    y += 1
    trees =[int(tree) for tree in [*row]]
    gridEastWest[y] = trees
    x = 0
    for tree in trees:
        x += 1
        if not x in gridNorthSouth:
            gridNorthSouth[x] = [tree]
        else:
            gridNorthSouth[x].append(tree)

maxX = len(gridEastWest[1])
maxY = len(gridNorthSouth[1])
print("Grid(%s x %s) read." % (maxX, maxY))
debug(gridEastWest)
debug(gridNorthSouth)
visibleTrees = []
for x in range(maxX):
    for y in range(maxY):
        EWrow = gridEastWest[y+1]
        lookEast = EWrow[x:]
        lookWest = EWrow[0:x+1]
        lookWest.reverse()
        NSrow = gridNorthSouth[x+1]
        lookNorth = NSrow[0:y+1]
        lookNorth.reverse()
        lookSouth = NSrow[y:]

        debug("  %s x %s" % (x, y))
        debug("    %s" % lookEast)
        debug("    %s" % lookWest)
        debug("    %s" % lookNorth)
        debug("    %s" % lookSouth)

        visibleSides = [v for v in [isVisible(lookDir) for lookDir in [lookEast, lookWest, lookNorth, lookSouth]] if v]
        debug("    has %s visible sides: %s" % (len(visibleSides), visibleSides))
        if len(visibleSides) > 0:
            visibleTrees.append((x, y))

print("Num visible trees: %s" % len(visibleTrees))