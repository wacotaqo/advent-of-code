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

iterations = 0
while ops:
    line = ops.popleft()
    (left, right) = line.split(' -> ')
    #print("%s ,%s" % (left, right))
    left_parts = left.split(' ')
    if len(left_parts) == 1: # variable assignment
        try:
            variables[right] = int(left)
        except:
            #print("Looking for assignee: %s" % left)
            if left in variables:
                variables[right] = variables[left]
            else:
                ops.append(line)
    elif left_parts[0] == 'NOT': # do NOT operation
        if left_parts[1] in variables:
            variables[right] = ~variables[left_parts[1]]
        else:
            ops.append(line)
    elif left_parts[1] == 'AND': # do AND operation
        if left_parts[0] in variables and left_parts[2] in variables:
            variables[right] = variables[left_parts[0]] & variables[left_parts[2]]
        else:
            ops.append(line)
    elif left_parts[1] == 'OR': # do OR operation
        if left_parts[0] in variables and left_parts[2] in variables:
            variables[right] = variables[left_parts[0]] | variables[left_parts[2]]
        else:
            ops.append(line)
    elif left_parts[1] == 'LSHIFT': # do OR operation
        if left_parts[0] in variables:
            variables[right] = variables[left_parts[0]] << int(left_parts[2])
        else:
            ops.append(line)
    elif left_parts[1] == 'RSHIFT': # do OR operation
        if left_parts[0] in variables:
            variables[right] = variables[left_parts[0]] >> int(left_parts[2])
        else:
            ops.append(line)
    else:
        print("Unknown instructions: %s --> %s" %  (left, right))

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