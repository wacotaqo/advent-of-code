# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re

# Read the input file
filename = "adventofcode2022_day05_input.txt"
#filename = "adventofcode2022_day05_input_test.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

MODE_CRATES = 0
MODE_INSTRUCTIONS = 1
CRATE_INPUT_SIZE = 4
CRATE_INPUT_PAD = " " * CRATE_INPUT_SIZE


def get_print_columns(crate_columns, extra_text=''):
    num_crate_columns = len(crate_columns)
    max_column_height = max([len(column) for column in crate_columns])

    # Pad each column to the max height
    print_columns = []
    for row in crate_columns:
        new_row = row[:]
        for i in range(max_column_height - len(row)):
            new_row.append('   ')
        print_columns.append(new_row)

    # Transpose the columns back to printable rows
    print_rows = [[print_columns[j][i] for j in range(len(print_columns))] for i in range(len(print_columns[0]))]
    print_rows.reverse()
    print_rows = [' '.join(row).rstrip() for row in print_rows]

    # Make the last row: Which is the column numbers
    last_row = []
    for i in range(0, len(crate_columns)):
        istr = ' %s' % str(i+1).ljust(2)
        last_row.append(istr)
    print_rows.append(' '.join(last_row).rstrip())

    return print_rows

def print_crate_columns(crate_columns, extra_text=''):
    print("")
    print("Crates: %s" % extra_text)
    print_rows = get_print_columns(crate_columns)
    for row in print_rows:
        print("->%s<-" % row)

# parse 1
mode = MODE_CRATES
crate_input = []
instruction_input = []
for row in assignment_input:
    if len(row) > 0 and row[0] == '#': continue # Skip comment

    if mode == MODE_CRATES:
        if row == '': # Empty line means the end of the crate setup. Start reading instructions
            mode = MODE_INSTRUCTIONS
            continue
        else:
            crate_input.append(row)
    elif mode == MODE_INSTRUCTIONS:
        instruction_input.append(row)
    else:
        print('Should not be here! (%s, %s)' % (mode, row))


# STEP 1: PARSE OUT THE COLUMNS

# Number of crates is last number in last row
# 1 2 3 4 5 => 5
num_crate_columns = int(crate_input[-1].split(' ')[-1])

# Split crates columns
crate_rows = []
for row in crate_input[:-1]:
    row_list = [row[i:i+CRATE_INPUT_SIZE] for i in range(0, len(row), CRATE_INPUT_SIZE)]
    for i in range(num_crate_columns - len(row_list)):
        row_list.append(CRATE_INPUT_PAD)
    #print(row_list)
    crate_rows.append(row_list)

#print("Rows: %s" % (crate_rows))

# Transpose to make list of columns
crate_columns = [[crate_rows[j][i] for j in range(0, len(crate_rows))] for i in range(len(crate_rows[0]))]
#print("Columns: %s" % (crate_columns))
def reverse_row(row, i):
    row[i].reverse()
list(map(lambda i:reverse_row(crate_columns, i), range(0, len(crate_columns))))
#print("Columns (1st try): %s" % (crate_columns))

# New way to do the above Transpose (try another way for fun). Just invert the range in the j loop
# and clean content at the same time
crate_columns = [[crate_rows[j-1][i].replace(' ','') for j in range(len(crate_rows), 0, -1) if len(crate_rows[j-1][i].replace(' ',''))>0] for i in range(len(crate_rows[0])) ]

#print("Columns: %s" % (crate_columns))
#print("Crates\n%s" % crate_input)

print_crate_columns(crate_columns, "Loaded %d columns of crates" % num_crate_columns)



# PARSE OUT THE INSTRUCTIONS AND EXECUTE
print("")
print("Processing %d Instructions" % len(instruction_input))
regex_move_row = re.compile(r'move (\d+) from (\d+) to (\d+)')
instructions = []
for instruction_row in instruction_input:
    re_result = regex_move_row.match(instruction_row)
    if re_result.groups():
        (move_crates, move_from, move_to) = re_result.groups()
        instructions.append((int(move_crates), int(move_from), int(move_to)))
    else:
        print("Unable to understand instruction: %s" % intruction_row)

moves = 0
for (move_crates, move_from, move_to) in instructions:
    moves += 1
    #print_crate_columns(crate_columns, '(move %d) Before moving %d from %d to %d.' % (moves, move_crates, move_from, move_to))
    for i in range(move_crates):
        crate_columns[move_to-1].append(crate_columns[move_from-1].pop())

print_crate_columns(crate_columns, 'Final state')

# NOW REPORT THE TOP CRATE ON EACH COLUMN
top_crates = [column[-1].replace('[','').replace(']','') for column in crate_columns]

print("")
print("Result - Top crates : %s" % ''.join(top_crates))

'''
# original input
print("")
for i in crate_input:
    print("->%s<-" % i)
'''