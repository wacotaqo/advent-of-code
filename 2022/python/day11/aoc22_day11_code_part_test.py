# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
from collections import defaultdict
from functools import reduce
import re
import decimal

decimal.getcontext().prec = 100000000000000000
decimal1 = decimal.Decimal(1)

filename = "adventofcode2022_day11_input.txt"
filename = "adventofcode2022_day11_input_test.txt"

DEBUG = 1
def debug(msg):
    if DEBUG:
        print(msg)

def get_factors_D(n):
    '''returns the prime factorization of a number; author: Wazim Karim'''
    factors=[]
    i = decimal.Decimal(2)
    while n >= i:
        d = n % i
        if d == 0:
            factors.append(i)
            n = n//i
            i = decimal.Decimal(2)
        else:
            i = i+1
    return factors

def mul_factors(f):
    return reduce(lambda x,y:x*y, f)

class Worry:
    def __init__(self, value):
        if type(value) == type(1) or type(value) == type(decimal1):
            self.worry = value
        else:
            raise TypeError("Unexpected type: %s " % value)

    def get_value(self):
        return self.worry

    def __add__(self, other):
        self.worry += other
        return self

    def __mul__(self, other):
        if type(other) == type(1) or type(other) == type(decimal1):
            self.worry = self.worry * other
        else:
            self.worry = self.worry * other.get_value()
        return self

    def has_factor(self, f):
        debug("check factor: %s %s %s" % (self, self.worry, f))
        return self.worry % f == 0

    def __str__(self):
        return 'Worry(%s)' % (self.worry)

class FWorry:
    def __init__(self, value):
        if type(value) == type(1) or type(value) == type(decimal1):
            self.worry = get_factors_D(value)
            self.worry.sort()
        elif type(value) == type([]):
            self.worry = value
        else:
            raise TypeError("Unexpected type: %s " % value)

    def get_value(self):
        return mul_factors(self.worry)

    def __add__(self, other):
        # Assuming number
        self.worry = get_factors_D(mul_factors(self.worry) + other)
        self.worry.sort()
        return self

    def __mul__(self, other):
        if type(other) == type(1) or type(other) == type(decimal1):
            self.worry.append(other)
        else:
            self.worry.extend(other.worry)
        self.worry.sort()
        return self

    def has_factor(self, f):
        return f in self.worry

    def __str__(self):
        return 'Worry(%s = %s)' % (self.worry, self.get_value())

class MonkeyItems:
    def __init__(self, items=[]):
        self.items = items

    def pop(self, index=None):
        if index:
            return self.items.pop(index)
        else:
            return self.items.pop()

    def append(self, item):
        self.items.append(item)

    def __str__(self):
        return "MonkeyItems(%s)" % str([str(i) for i in self.items])

    def __len__(self):
        return len(self.items)


fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

monkeys = {}
for i in range(0, len(assignment_input), 7):
    mip = [i.split(':') for i in assignment_input[i:i+7]]
    #debug(mip)

    m = int(re.findall("\d+", mip[0][0])[0])
    #debug("monkey: %s = > %s" % (mip[0], m))

    si = [decimal.Decimal(i) for i in mip[1][1].split(',')]
    si = MonkeyItems([FWorry(i) for i in si])
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
    if 1: #r % 100 == 0:
        print("Round: %s" % r)
        for i in range(0, len(monkeys)):
            debug("Monkey %s inspects %s" % (i, monkeys[i]['inspects']))

    for i in range(0, len(monkeys)):
        #debug("before %s" % i)
        #debug("  %s" % (str(monkeys[i])))

        m = monkeys[i]
        for j in range(len(m['items'])):
            old = m['items'].pop(0)
            m['inspects'] += 1
            new = eval(m['instruction'])
            if new.has_factor(m['test']):
                #debug("  test: %s %% %s = %s ==> true ==> adding %s to monkey %s" % (new, m['test'], new % m['test'], new, m['ontrue']))
                monkeys[m['ontrue']]['items'].append(new)
            else:
                #debug("  test: %s %% %s = %s ==> true ==> adding %s to monkey %s" % (new, m['test'], new % m['test'], new, m['onfalse']))
                monkeys[m['onfalse']]['items'].append(new)
        #debug("after")
        #for i in range(0, len(monkeys)):
        #    debug("  %s" % (str(monkeys[i]['items'])))
    #debug("After round %s" % r)
    #for i in range(0, len(monkeys)):
    #    debug("  %s" % (str(monkeys[i]['items'])))

#debug(monkeys)

debug("")
result = [monkeys[i]['inspects'] for i in range(len(monkeys))]
result.sort()
result = result[-2] * result[-1]
for i in range(0, len(monkeys)):
    debug("%s inspects %s" % (i, monkeys[i]['inspects']))
debug(result)