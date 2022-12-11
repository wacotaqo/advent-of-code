# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
from collections import defaultdict
import re

filename = "adventofcode2022_day11_input.txt"
#filename = "adventofcode2022_day11_input_test.txt"

DEBUG = 0
def debug(msg):
    if DEBUG:
        print(msg)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

monkeys = {}
for i in range(0, len(assignment_input), 7):
    mip = [i.split(':') for i in assignment_input[i:i+7]]
    #debug(mip)

    m = int(re.findall("\d+", mip[0][0])[0])
    #debug("monkey: %s = > %s" % (mip[0], m))

    si = [int(i) for i in mip[1][1].split(',')]
    #debug("items: %s" % str(si))

    ins = mip[2][1].split('=')[1].strip()
    #debug("instruction: %s" % ins)

    tst = int(re.findall('\d+', mip[3][1])[0])
    #debug("test divisible by: %s" % tst)

    ont = int(re.findall('\d+', mip[4][1])[0])
    onf = int(re.findall('\d+', mip[5][1])[0])
    #debug("on true: %s, on false: %s" % (ont, onf))

    monkey = {
        'name' : m,
        'items': si,
        'instruction': ins, # new = *
        'test': tst,
        'ontrue': ont,
        'onfalse': onf,
        'inspects': 0
    }
    monkeys[m] = monkey

for r in range(0, 20):
    for i in range(0, len(monkeys)):
        m = monkeys[i]
        for j in range(len(m['items'])):
            old = m['items'].pop(0)
            m['inspects'] += 1
            new = eval(m['instruction'])//3
            if new % m['test'] == 0:
                monkeys[m['ontrue']]['items'].append(new)
            else:
                monkeys[m['onfalse']]['items'].append(new)
    debug("After round %s" % r)
    for i in range(0, len(monkeys)):
        debug("  %s" % (str(monkeys[i]['items'])))

debug("")
result = [monkeys[i]['inspects'] for i in range(len(monkeys))]
result.sort()
result = result[-2] * result[-1]
for i in range(0, len(monkeys)):
    print("%s inspects %s" % (i, monkeys[i]['inspects']))
print(result)