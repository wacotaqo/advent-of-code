import os
filename = "aoc2015_day05_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

#lines = ['ugknbfddgicrmopn', 'aaa', ]

print("%s lines read." % (len(lines)))
print("First 12 lines: %s" % lines[:12])


vowels = 'aeiou'
exclude = ['ab', 'cd', 'pq', 'xy']
nice_strings = []
for i, word in enumerate(lines):
    #print("Try word %s: %s" % (i, word))
    next = False
    has_repeats = False
    cnt_vowels = 0
    for e in exclude:
        if e in word:
            next = True
            continue
    if next:
        continue
    last_letter = ''
    for l in word:
        if l in vowels:
            cnt_vowels += 1
        if l == last_letter:
            has_repeats = True
        last_letter = l
    if cnt_vowels > 2 and has_repeats:
        nice_strings.append(word)
        
print("Found %s nice strings" % len(nice_strings))
print("First 12 nice strings: %s" % nice_strings[:12])