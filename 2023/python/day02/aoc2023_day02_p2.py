# This program is an exercise/challenge from the 2023 advent of code competition
#
#
import os
from functools import reduce

filename = "adventofcode2023_day02_input.txt"

DEBUG = 0
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

debug("Input read: %s " % assignment_input)
debug("Input lines: %s" % len(assignment_input))
games = []
games_power = []

def process_input(input):
    for line in input:
        debug(line.split(':'))
        (game, sets) = line.split(':')
        (_, game) = game.split(' ')
        games.append(game)
        debug(game)
        game_cubes_min = {'red': 0, 'green': 0, 'blue': 0}
        for set in sets.split(';'):
            subsets = set.split(',')
            for subset in subsets:
                (cube_cnt, cube_color) = subset.strip().split(' ')
                cube_cnt = int(cube_cnt)
                if game_cubes_min[cube_color] < cube_cnt: 
                    game_cubes_min[cube_color] = cube_cnt
        debug((game, sets, game_cubes_min))

        game_power = reduce((lambda x, y: x * y), game_cubes_min.values())
        games_power.append(game_power)

    print("process_input_done")
    
process_input(assignment_input)

print("num games: %s" % len(games))
print("sum of game powers: %s" % sum(games_power))


