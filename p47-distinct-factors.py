# A lot of solutions in the forum are awful, but the fastest one seems to be to work up an array of factors[] starting from 2 and multiplying out by earlier entries in factors[] to create later entries

from sieve import eratosthenes
from math import sqrt
prime_maker = eratosthenes()
primes = [prime_maker.next()]

def factors(n):
    results = []
    candidate = primes
    done = False
    while primes[-1] < sqrt(n):
        primes.append(prime_maker.next())
    while not done:
        for p in primes:
            if p > sqrt(n):
                done = True
                break
            if n % p == 0:
                results.append(p)
                n = n/p
                break
    if n:
        results.append(n)
    return results
           
i = 600   
run = 0       
while True:
    i += 1
    if len(set(factors(i))) == 4:
        run += 1
    else:
        run = 0
    if run == 4:
        print i
        break