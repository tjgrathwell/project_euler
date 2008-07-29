from sieve import eratosthenes
prime_maker = eratosthenes()

fifty_million = 50000000

twos = {}
threes = {}
fours = {}
while True:
    prime = prime_maker.next()
    squared = prime * prime
    if squared >= fifty_million: break
    twos[prime] = squared

for prime in sorted(twos.keys()):
    cubed = twos[prime] * prime
    if cubed >= fifty_million: break
    threes[prime] = cubed
    
for prime in sorted(twos.keys()):
    quad = threes[prime] * prime
    if quad >= fifty_million: break
    fours[prime] = quad

winners = {}
for square in twos.values():
    for cube in threes.values():
        for quad in fours.values():
            candidate = square + cube + quad
            if candidate < fifty_million:
                winners[candidate] = 1
                
winning_numbers = winners.keys()
print len(winning_numbers)