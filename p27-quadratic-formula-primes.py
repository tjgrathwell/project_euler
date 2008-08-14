# We want a formula n**2 + a*n + b where abs(a) and abs(b) are less than 1000 that generates the maximal value of primes when marching up n from 0
# Since n=0 drops that formula to just 'b', 'b' has to be a prime, for starters
# Additionally, for n=1, 1 + a will become odd for an even a, and adding an odd number to your odd prime makes an even number which will never be prime.
# So we should be able to take every prime 'b' along with every odd a from -999 to 999 and see how many primes the formula generates before cracking

from sieve import eratosthenes
prime_maker = eratosthenes()
primes = []
for i in xrange(1000):
    primes.append(prime_maker.next())

def how_many_primes(a,b):
    n = 0
    while True:
        val = n ** 2 + a * n + b
        while val > primes[-1]:
            primes.append(prime_maker.next())
        if val not in primes:
            break
        n += 1
    return n

the_most = 0
ma, ma = 0, 0
small_primes = [p for p in primes if p < 1000]
for b in small_primes:
    for a in xrange(-999,1000,2):
        how_many = how_many_primes(a,b)
        if how_many > the_most:
            the_most = how_many
            ma, mb = a,b

print the_most, ma, mb