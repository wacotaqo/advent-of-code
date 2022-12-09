# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os

filename = "adventofcode2022_day08_input.txt"
#filename = "adventofcode2022_day08_input_test.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

DIR_NORTH = (0, -1)
DIR_EAST = (1, 0)
DIR_SOUTH = (0, 1)
DIR_WEST = (-1, 0)
ALL_DIRECTIONS = (DIR_NORTH, DIR_EAST, DIR_SOUTH, DIR_WEST)

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

class Tree:
    def __init__(self, x, y, height):
        self.posX = x
        self.posY = y
        self.height = height
        self.onTheEdge = False

    def getNeighbourTrees(self, grid, directions=ALL_DIRECTIONS):
        return [tree for tree in [grid.getTreeByPosition(self.posX + scanX, self.posY + scanY) for (scanX, scanY) in ALL_DIRECTIONS] if tree]

    def isTreeHeightMaxInDir(self, height, direction, grid):
        if height >= self.height:
            debug("     %s is short(%s) enough. Will look further %s." % (self, height, direction))
            (dirX, dirY) = direction
            neighbour = grid.getTreeByPosition(self.posX + dirX, self.posY + dirY)
            if neighbour:
                return neighbour.isTreeHeightMaxInDir(height, direction, grid)
            else:
                debug("    At the edge. Height was sufficient!")
                return True
        else:
            debug("     %s is blocking visibility(%s). :-(" % (self, height))
            return False

    def isVisible(self, grid, directions=ALL_DIRECTIONS):
        debug("For %s , will check visibility in directions %s" % (self, ALL_DIRECTIONS))
        visibleDirections = []
        for direction in directions:
            debug("    direction: %s" % str(direction))
            (dirX, dirY) = direction
            neighbour = grid.getTreeByPosition(self.posX + dirX, self.posY + dirY)
            if neighbour:
                if self.height > neighbour.height:
                    debug("      taller(%s) than neighbour(%s)" % (self.height, neighbour.height))
                    if neighbour.isTreeHeightMaxInDir(self.height-1, direction, grid):
                        debug("      and tallest in direction %s" % str(direction))
                        visibleDirections.append(direction)
                    else:
                        debug("      not tallest in direction %s" % str(direction))
                else:
                    debug("      not taller(%s) than neighbour(%s)" % (self.height, neighbour.height))
            else:
                debug("      at edge...")
                visibleDirections.append(direction)
        visible = len(visibleDirections) > 0 #"== len(directions)
        if visible:
            debug("    I am visible!")
        else:
            debug("    I am not visible (%s)" % (visibleDirections))
        return visible

    def __str__(self):
        output = "Tree(Pos=(%s, %s), Height=%s, OnEdge=%s)" % (self.posX, self.posY, self.height, self.onTheEdge)
        return output

class PatchOfTrees:
    def __init__(self, map):
        self.grid = []
        self.gridXMax = 0
        self.gridYMax = len(map)
        y = 0
        for row in map:
            y += 1
            x = 0
            self.gridXMax = len(row)
            treeRow = []
            for treeHeight in row:
                x += 1
                tree = Tree(x, y, int(treeHeight))
                if x == 1 or y == 1 or x == self.gridXMax or y == self.gridYMax:
                    tree.onTheEdge = True
                treeRow.append(tree)
            self.grid.append(treeRow)

    def getTreeByPosition(self, x, y):
        if x <= 0 or x > self.gridXMax or y <= 0 or y > self.gridYMax:
            return None
        else:
            return self.grid[y-1][x-1]

    def getVisibleTrees(self):
        visibleTrees = []
        for row in self.grid:
            for tree in row:
                if tree.isVisible(self):
                    visibleTrees.append(tree)
        return visibleTrees

    def numTrees(self):
        return sum([len(row) for row in self.grid])

pot = PatchOfTrees(assignment_input)
print(assignment_input)
print("Patch has %s trees on an %s,%s grid." % (pot.numTrees(), pot.gridXMax, pot.gridYMax))
visibleTrees = pot.getVisibleTrees()
print("Visible trees: %s" % (len(visibleTrees)))