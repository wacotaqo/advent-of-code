import os
filename = "aoc2015_day05_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

#lines = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
#lines = ['zztdcqzqddaazdjp', 'xyxyx', 'xyxgx', 'xyajasdkalssdxy', 'xyajbsdkalssdxy', 'xyajaxdykalssdy', 'aaada', 'aaadaaa']

print("%s lines read." % (len(lines)))
print("First 12 lines: %s" % lines[:12])


vowels = 'aeiou'
exclude = ['ab', 'cd', 'pq', 'xy']
nice_strings = []
for i, word in enumerate(lines):
    #print("Try word %s: %s" % (i, word))
    repeat_after_2 = False
    double_repeat = False
    for j in range(len(word)):
        if j > 1:
            if word[j] == word[j-2]:
                repeat_after_2 = word[j-2:j+1]
                #print("Found repeat of %s" % word[j-2:j+1])
        if j > 0:
            pair = word[j-1:j+1]
            if j > 0:
                leftovers = word[0:j-1] + ' ' + word[j+1:]
            else:
                leftovers = word[j+1:]
            #print("Testing pair: %s in %s" % (pair, leftovers))
            if pair in leftovers:
                double_repeat = pair
                #print("Found double! %s in %s" % (pair, word))
    if repeat_after_2 and double_repeat:
        nice_strings.append((word, repeat_after_2, double_repeat))
        #print("Found nice word: %s" % word)
print("Found %s nice strings" % len(nice_strings))
print("First 12 nice strings: %s" % nice_strings[:12])