import os
import re

filename = "aoc2015_day06_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()
size = 1000

test = 0
if test:
    size = 10
    lines = ['turn on 0,0 through 5,5', 'toggle 4,4 through 8,9', 'turn off 2,2 through 3,3']

instruction_pattern = re.compile('([a-z ]+) ([0-9,]+) through ([0-9,]+)')

lights = [[' ' for _ in range(1000)] for _ in range(1000)]
for line in lines:
    mo = instruction_pattern.match(line)
    if mo:
        (instruction, from_pt, to_pt) = mo.groups()
        (fromx, fromy) = [int(n) for n in from_pt.split(',')]
        (tox, toy) = [int(n) for n in to_pt.split(',')]
        if test:
            print(line)
            print("%s %s,%s --> %s,%s" % (instruction, fromx, fromy, tox, toy))
        for x in range(fromx, tox+1):
            for y in range(fromy, toy+1):
                if instruction == 'toggle':
                    if lights[x][y] == ' ':
                        lights[x][y] = '*'
                    else:
                        lights[x][y] = ' '
                elif instruction == 'turn on':
                    lights[x][y] = '*'
                elif instruction == 'turn off':
                    lights[x][y] = ' '
                else:
                    print("Should not come here: Unknown instruction! %s" % instruction)
                    assert False
    else:
        print('Bad line: %s' % line)
        assert False

cnt_lights = 0
for x in range(1000):
    for y in range(1000):
        if lights[x][y] == '*':
            cnt_lights += 1
print("number of lights on: %s" % cnt_lights)

