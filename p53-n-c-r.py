fac = lambda n:reduce(lambda a,b:a*(b+1),range(n),1)

def combo(n, r):
    return fac(n) / (fac(r) * fac(n-r))
    
total = 0
for n in xrange(1,101):
    for r in xrange(1,n):
        if combo(n,r) > 1000000:
            total += 1
print total