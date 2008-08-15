max, mi, mj = 0, 0, 0
for i in xrange(1,101):
    for j in xrange(1,101):
        res = sum([int(n) for n in str(i ** j)]) 
        if res > max:
            max = res
            mi, mj = i,j
            
print max, mi, mj