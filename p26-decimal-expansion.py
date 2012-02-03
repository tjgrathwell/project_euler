# this solution is THE WORST and takes like 30 seconds to do

# better solutions from the forums include:
#   * re-implementing long division and noting when you see a cycle
#   * using the properties of MATHS and something to do with powers
#     of ten (probably wikipedia "decimal expansion")

from decimal import Decimal, getcontext
from collections import defaultdict

MAX_DIGITS = 10000

getcontext().prec = MAX_DIGITS + 10

guesses = defaultdict(list)

def test_guess(decimal, guess):
    guess_length = len(guess)
    decimal = decimal[guess_length:]
    while len(decimal) > len(guess):
        if guess != decimal[:guess_length]:
            return False
        decimal = decimal[guess_length:]
    return True

def get_guess(decimal):
    for guess_length in xrange(1, MAX_DIGITS/3):
        guess = decimal[:guess_length]
        if test_guess(decimal, guess):
            return guess
    if len(decimal) == 1:
        return False
    return get_guess(decimal[1:])

counts = {}

for i in xrange(2,1000):
    dec = Decimal(1.0) / i
    stringied = str(dec)
    after_dot = stringied[stringied.index('.')+1:]

    guess = get_guess(after_dot)
    counts[i] = len(guess)

# here is where I forgot how to sort lists backwards

counts_reversed = defaultdict(list)

for k, v in counts.items():
    counts_reversed[v].append(k)

for k in sorted(counts_reversed.keys()):
    if k > 500:
        print k, counts_reversed[k]

# apparently it's not 982
