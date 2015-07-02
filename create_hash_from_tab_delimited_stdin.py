import sys
import hashlib

# reads tab-delimited input from stdin and prints
# the first item in the string, a tab, and the
# hashed version of the entire input line

while True:
    line = sys.stdin.readline()
    line = line.strip()
    if not line:
        break
    hcs = line.split('\t')

    print len(hcs)
    for field in hcs:
        if len(field):
            #print field
            scrunched = "".join(field)
            hashed = str(hashlib.md5(scrunched).hexdigest())
    print str(hcs[0]) + '\t' + str(hashed)
