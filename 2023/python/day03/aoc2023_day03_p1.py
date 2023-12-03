# This program is an exercise/challenge from the 2023 advent of code competition
#
#
import os
import re

filename = "adventofcode2023_day03_input.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

#debug("Input read: %s " % assignment_input)
debug("Input lines: %s" % len(assignment_input))

values = []

def make_grids_NS_EW(input): ## Not used
    gridEastWest = {}
    gridNorthSouth = {}
    y = 0
    for row in input:
        y += 1
        items = [*row]
        gridEastWest[y] = items
        x = 0
        for item in items:
            x += 1
            if not x in gridNorthSouth:
                gridNorthSouth[x] = [item]
            else:
                gridNorthSouth[x].append(item)
    return (gridEastWest, gridNorthSouth)

def make_item_map(input):
    items = []
    item_map = {}
    y = 0
    for row in input:
        y += 1
        debug("row %s length: %s" % (y, len(row)))
        row_chars = [*row]
        item_map[y] = {} # prepare empty row number y
        x = 0
        item = ''
        last_type = ''
        for row_char in row_chars:
            x += 1

            if row_char == '.':
                this_type = ''
            elif row_char.isnumeric():
                this_type = 'n'
            else:
                this_type = 's'

            if last_type == this_type and this_type != '':
                item += row_char
            elif last_type == '' and this_type in ('n', 's'):
                item = row_char
            else: 
                # type has changed, save the last item if it excists
                if item:
                    item_x = x - len(item)
                    items.append((last_type, item, y, item_x)) # Add the item, the coordinates (row and the start colum)
                    item_map[y][item_x] = (last_type, item)
                    item = ''
                # start collecting the new item
                if this_type != '':
                    item = row_char

            last_type = this_type

        if item: 
            item_x = x - len(item)
            items.append((last_type, item, y, item_x)) # Add the item, the coordinates (row and the start colum)
            item_map[y][item_x] = (last_type, item)

    return items, item_map

def process_input(input):
    (items, item_map) = make_item_map(input)

    nums = []

    for (item_type, item, item_y, item_x) in items: 
        if item_type == 'n':
            debug("Item: %s at %s, %s. Looking for adjacent symbol" % (item, item_x, item_y))
            debug("verify map %s, %s = %s" % (item_x, item_y, item_map[item_y][item_x]))
            has_adj_symbol = False
            for row in range(item_y-1, item_y+2):
                for col in range(item_x-1, item_x+len(item)+1):
                    if row in item_map.keys():
                        if col in item_map[row].keys():
                            if item_map[row][col][0] == 's': 
                                has_adj_symbol = True
                                debug("  Found symbol: %s" % str(item_map[row][col]))
            if has_adj_symbol: 
                nums.append(int(item))      

    print("%s numbers have adjacent symbols" % len(nums))
    print(nums)
    print("Sum of these numbers are %s" % sum(nums))
    #print(items)

    print("process_input_done")
    
process_input(assignment_input)#[0:4])
print("result: %s" % values)