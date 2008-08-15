# Conjecture is that every prime can be written as the sum of a prime and 2 * the square of some number
# Brute force is to roll through primes and try to construct them based off this rule

# Per the forums, a more efficient way is to subtract the squares from each odd composite and check for primeness, rather than building up on top of existing primes. Oh well.

from sieve import eratosthenes
prime_maker = eratosthenes()
primes = [prime_maker.next()]

i = 9
while True:
    while i > primes[-1]:
        primes.append(prime_maker.next())
    if i in primes:
        i += 2
        continue
    
    found = False
    for p in primes:
        n = 1
        while True:
            computed = p + 2 * (n ** 2)
            if computed == i:
                found = True # '%d == %d + 2 * (%d ** 2)' % (i, p, n)
            if computed > i:
                break
            n += 1
    if not found:
        print 'fail at ', i
        break
    
    i += 2