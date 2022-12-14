import os
from collections import deque

filename = "aoc2015_day07_input.txt"
#filename = "aoc2015_day07_input_test.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

variables = {}
ops = deque(lines)

def eval_value(v):
    if v.isnumeric():
        return int(v)
    else:
        return variables[v]
        
def eval_expression(parts):
    if len(parts) == 1: # handle as assignment
        part = parts[0]
        return eval_value(part)
    elif parts[0] == 'NOT': # do AND operation
        return ~ eval_value(parts[1])
    elif parts[1] == 'AND': # do AND operation
        return eval_value(parts[0]) & eval_value(parts[2])
    elif left_parts[1] == 'OR': # do OR operation
        return eval_value(parts[0]) | eval_value(parts[2])
    elif left_parts[1] == 'LSHIFT': # do Left Shift operation
        return eval_value(parts[0]) << eval_value(parts[2])
    elif left_parts[1] == 'RSHIFT': # do Right Shift operation
        return eval_value(parts[0]) >> eval_value(parts[2])
    else:
        raise Exception("Unknown instructions: %s --> %s" %  (left, right))
        
iterations = 0
while ops:
    line = ops.popleft()
    (left, right) = line.split(' -> ')
    #print("%s ,%s" % (left, right))
    left_parts = left.split(' ')
    try:
        variables[right] = eval_expression(left_parts)
    except KeyError:
        ops.append(line)

    iterations += 1
    if iterations % 100 == 0:
        print("Iteration %s: ops %s" % (iterations, len(ops)))

    if iterations > 10000:
        break

vars = list(variables.keys())
vars.sort()
for v in vars:
    if variables[v] < 0:
        variables[v] += 65536
    print("%s = %s" % (v, variables[v]))

if ops:
    for i in ops:
        print(i)