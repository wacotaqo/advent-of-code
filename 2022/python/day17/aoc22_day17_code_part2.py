# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
from collections import deque, defaultdict
from functools import reduce

filename = "adventofcode2022_day17_input.txt"
filename = "adventofcode2022_day17_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

shape_list = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""

space_floor = list('+-------+')
shape_start_x = 3
AIRJET_MOVE_X = {'<': -1, '>': 1}

combinations = 0


def new_empty_row():
    return list('|.......|')

class Space:
    # Represents the space for the shapes to fall.
    # with the floor being at row/y = 0
    # and each row above being y+1 of the row below
    def __init__(self):
        self.space = defaultdict(new_empty_row)
        self.space[0] = space_floor # Place floor at y = 0
        self.space[1] = new_empty_row()
        self.airjet = 0
        self.last_highest = 0
        self.remember = {}
        self.combinations_last_highest = 0
        self.combinations_last_row = None

    def __str__(self):
        return "Space(%s)" % str(self.space.items())

    def get_highest_occupied_y(self):
        y = self.last_highest
        while 1:
            if self.space[y] == new_empty_row():
                self.last_highest = y-1
                return self.last_highest
            y += 1

    def get_shape_starting_y(self, empty_rows=3):
        return self.get_highest_occupied_y() + empty_rows + 1

    def check_shape_fits(self, shape, x, y):
        #print("    Check shape fits at %s, %s (%s)" % (x, y, shape))
        fits = 0
        for (sx, sy) in shape.pts:
            cx = sx + x
            cy = sy + y
            #print("      Check %s,%s in row %s [%s]" % (cx, cy, cy, ''.join(self.space[cy])))
            fits +=  self.space[cy][cx] == '.'
        return fits == len(shape.pts)

    def drop_shape(self, rock, shape, start_x, start_y, airjets):
        at_rest = False
        x = start_x
        y = start_y

        if 0:
            if rock % combinations == 0:
                highest_y = self.get_highest_occupied_y()
                self.combinations_last_row = ''.join(self.space[highest_y])
                height_diff = highest_y - self.combinations_last_highest
                if self.combinations_last_row in self.remember:
                    print("Repeat ", self.combinations_last_row, rock, self.remember[self.combinations_last_row])
                    print("highest %s rock %s" % (highest_y, rock))

                # When we know what to do, we can do it here...

                self.remember[self.combinations_last_row] = height_diff # Number of additional rocks for this combination
                self.combinations_last_highest = highest_y
                print(self.remember)

        if 1:
            if rock % combinations == 0:
                move = self.airjet #AIRJET_MOVE_X[airjets[self.airjet]]
                if self.combinations_last_row: # If we have been here before, start doing something...
                    combo = (shape.id, move, self.combinations_last_row)
                    if combo in self.remember:
                        print("Repeat", combo, self.remember[combo])

                highest_y = self.get_highest_occupied_y()
                self.combinations_last_row = ''.join(self.space[highest_y])
                height_diff = highest_y - self.combinations_last_highest
                self.combinations_last_highest = highest_y
                combo = (shape.id, move, self.combinations_last_row)
                if not combo in self.remember:
                    self.remember[combo] = {height_diff: 1}
                elif not height_diff in self.remember[combo]:
                    self.remember[combo][height_diff] = 1
                else:
                    self.remember[combo][height_diff] += 1



        #print("Drop at (%s, %s) shape %s" % (x, y, shape))
        if not self.check_shape_fits(shape, start_x, start_y):
            #print("Shape cannot be dropped here!")
            return

        while not at_rest:
            # Push by air jet
            (new_x, new_y) = (x + AIRJET_MOVE_X[airjets[self.airjet]], y)
            #print("  Check if it can move ..  %s  .." % (3 * airjets[self.airjet]))
            if self.check_shape_fits(shape, new_x, new_y):
                #print("    yes!")
                x = new_x
                y = new_y
            #else:
            #    print("    no :-(")
            self.airjet += 1
            if self.airjet >= len(airjets): self.airjet = 0

            # Fall
            (new_x, new_y) = (x, y-1)
            #print("    Now check if it can fall to (%x, %x)" % (new_x, new_y))
            at_rest = not self.check_shape_fits(shape, new_x, new_y)
            if not at_rest:
                x = new_x
                y = new_y
            #    print("      yes!")
            #else:
            #    print("      no :-("a)

        #print("Stopped at position: %s, %s" % (x, y))
        for (sx, sy) in shape.pts:
            (nx, ny) = (sx + x, sy + y)
            #print("set rock at %s, %s (base: %s, %s)" % (nx, ny, x, y))
            self.space[ny][nx] = '#'

        #print("Space looks like this now: ")
        #self.print_space()

    def print_space(self, y=0):
        print("Space (rockheight: %s)" % self.get_highest_occupied_y())
        if y:
            from_y = y
            to_y = y -1
        else:
            from_y = len(self.space)-1
            to_y = -1
        for y in range(from_y, to_y, -1):
            print("%7s  %s" % (y, ''.join(self.space[y])))

class Shape:
    def __init__(self, shape_str, id):
        self.id = id
        self.x = 0
        self.y = 0
        self.pts = []
        x = y = 0
        #print("(%s)" % shape_str)
        for c in shape_str:
            if c == '#': # add rock
                self.pts.append((x, y))
                x += 1
            elif c == '.': # skip air
                x += 1
            elif c == '\n': # next row
                y += 1
                x = 0
            else:
                assert "Should not be here. %s in %s" % (c, shape_str)

        # Invert y ordinates to orient around bottom, left = 0,0 and y increases upwards
        self.pts = [(x, y-oy) for (x,oy) in self.pts]

        self.length = x
        self.height = y+1

    def __str__(self):
        return 'Shape(%s (%s, %s)-(%s, %s), %s' % (self.id, self.x, self.y,self.length, self.height, self.pts)


fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()

shapes = [Shape(s.strip(), i) for i, s in enumerate(shape_list.split('\n\n'))]
num_shapes = len(shapes)
airjets = data
combinations = len(airjets) * num_shapes
space = Space()
rock = 0
rocks_to_drop = 200000000 # 1000000000000
while rock < rocks_to_drop:
    #if rocks % 100000 == 0: print(rocks)
    space.drop_shape(rock, shapes[rock % num_shapes], shape_start_x, space.get_shape_starting_y(), airjets)
    rock += 1

    #print("Rock\n====")
    #space.print_space(space.get_highest_occupied_y())

print("Shapes used: %s" % len(shapes))
for s in shapes:
    print(s)
print("")
print("Tower is %s rocks tall." % space.get_highest_occupied_y())
#space.print_space()
