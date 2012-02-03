from decimal import Decimal
from fractions import Fraction

pairs = []

def nth_char(num, n):
    return int(str(num)[n])

for top in xrange(10, 99):
    for bottom in xrange(top, 99):
        real_val = Decimal(top) / bottom

        if str(top)[1] == str(bottom)[1]:    continue # "trivial" case

        if str(top)[1] != str(bottom)[0]:    continue # not "cancelable"

        denom = nth_char(bottom,1)
        if denom and real_val == Decimal(nth_char(top,0)) / denom:
            pairs.append(Fraction(numerator=top, denominator=bottom))

print pairs

# [(16, 64), (19, 95), (26, 65), (49, 98)]

print reduce(lambda x,y: x*y, pairs)
