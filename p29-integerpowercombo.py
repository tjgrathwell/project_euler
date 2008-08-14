all = {}
for i in xrange(2,101):
    for j in xrange(2,101):
        all[i ** j] = 1
        
print len(all.keys())