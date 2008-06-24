import sys
from rabin_miller import rabin_miller

def triangle_row(num):
    # http://www.research.att.com/~njas/sequences/A000124
    n = num-1
    start = n * (n+1) / 2 + 1
    return range(start, start+n+1)

def neighbors(top, middle, bottom, n):
    while len(top) < len(bottom):    top += [False]
    while len(middle) < len(bottom): middle += [False]
    neighbors = 0
    if (n > 0):
        if bottom[n-1]: neighbors += 1
        if middle[n-1]: neighbors += 1
        if top[n-1]:    neighbors += 1
    if (n < len(middle)-1):
        if bottom[n+1]: neighbors += 1
        if middle[n+1]: neighbors += 1
        if top[n+1]:    neighbors += 1
    if bottom[n]: neighbors += 1
    if top[n]:    neighbors += 1
    return neighbors
  
primed = 0
def filter_prime(num):
    global primed
    primed += 1
    if primed % 10 == 0: print "prime candidate: " + str(num)
    if rabin_miller(num): return num
    return False

if len(sys.argv) < 2: exit(0)
row = int(sys.argv[1])
rows_of_interest = [triangle_row(r) for r in xrange(row-1, row+2)]
filtered_rows = []
for r in rows_of_interest:
    filtered_rows.append([filter_prime(num) for num in r])

for row in filtered_rows:
    print row

for i,n in enumerate(filtered_rows[1]):
    if n and neighbors(filtered_rows[0], filtered_rows[1], filtered_rows[2], i) > 1:
        print n