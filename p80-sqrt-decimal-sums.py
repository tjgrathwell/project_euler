# The resulting forum tells me Decimal(n).sqrt() works fine for this, but oh well...
# Some other joker mentioned
    # from gmpy import *
    # set_minprec(400) 

from math import sqrt, floor

def find_digit(left, right):
    # left = \d+X, right = Y
    # want to fill X with the largest value such that \d+X* X < Y
    for i in xrange(10):
        value = int(str(left) + str(i)) * i
        if value > right:
            return i-1
    return i

# This poor bastard could use a good refactoring, but it works as-is
def square_root(n,digits=10):
    # http://www.homeschoolmath.net/teaching/square-root-algorithm-example.php
    # Might be the same as http://en.wikipedia.org/wiki/Shifting_nth-root_algorithm
    strn = str(n)
    groups = []
    result = []
    for i in xrange(len(strn)/2):
        groups.append(strn[-2:])
        strn = strn[:-2]
    if strn:
        groups.append(strn)

    dividee = int(groups.pop())
    digit = int(floor(sqrt(dividee)))
    left = digit
    result.append(digit)
    for i in xrange(digits-1):
        if groups:
            next_group = int(groups.pop())
        else:
            next_group = 0
        right = 100 * (dividee - result[-1]*left) + next_group
        left = 2 * int(''.join([str(c) for c in result]))
        next_digit = find_digit(left, right)
        left = int(str(left) + str(next_digit))
        result.append(next_digit)
        dividee = right

    return result
    
perfects = [x**2 for x in xrange(1,11)]
print perfects
    
total = 0
for i in xrange(100):
    if i not in perfects:
        total += sum(square_root(i,100))
        
print total