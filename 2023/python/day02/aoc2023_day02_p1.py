# This program is an exercise/challenge from the 2023 advent of code competition
#
#
import os
import re

filename = "adventofcode2023_day02_input.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

debug("Input read: %s " % assignment_input)
debug("Input lines: %s" % len(assignment_input))

allowed_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

games = []
legit_games = []

def process_input(input):
    for line in input:
        #print(line.split(':'))
        (game, sets) = line.split(':')
        (_, game) = game.split(' ')
        games.append(game)
        #print(game)
        is_legit_game = True
        for set in sets.split(';'):
            subsets = set.split(',')
            for subset in subsets:
                (cube_cnt, cube_color) = subset.strip().split(' ')
                if allowed_cubes[cube_color] < int(cube_cnt):
                    is_legit_game = False
                    #print("game is not legit: %s" % subset)
        if is_legit_game: 
            legit_games.append(int(game))

        print(game, is_legit_game, sets)
    print("process_input_done")
    
process_input(assignment_input)

print("num games: %s" % len(games))
print("num legit games: %s" % len(legit_games))
print("sum legit game ids: %s" % sum(legit_games))

