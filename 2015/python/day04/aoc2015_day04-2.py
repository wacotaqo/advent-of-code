import os
import hashlib

filename = "aoc2015_day04_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
data = fh.read().strip()
fh.close()
lines = data.splitlines()

secret_key = data
#secret_key = 'abcdef'
for i in range(100000, 9999999):
    encode_str = "%s%s" % (secret_key, i)
    m = hashlib.md5()
    m.update(encode_str.encode('utf-8'))
    hash = m.hexdigest()
    if hash[:6] == '000000':
        print(i)
        break
    
