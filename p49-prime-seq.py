import sieve, sys

s = sieve.eratosthenes()
primes = []
while True:
    next = s.next()
    if next > 9999:
        break
    if next > 999:
        primes.append(next)

perm_dict = {}
for p in primes:
    dict_val = perm_dict.setdefault(''.join(sorted(str(p))), [])
    dict_val.append(p)
    
def choose_three(seq):
    for i in xrange(len(seq)-2):
        for j in xrange(i+1,len(seq)-1):
            for k in xrange(j+1,len(seq)):
                yield [seq[i], seq[j], seq[k]]
    
for k in perm_dict:
    l = perm_dict[k]
    if len(l) < 3:
        continue
    for seq in choose_three(l):
        if seq[1] - seq[0] == seq[2] - seq[1]:
            print seq, ''.join(str(i) for i in seq)