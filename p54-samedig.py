# python 2.5 not installed :(
def all(iterable):
     for element in iterable:
         if not element:
             return False
     return True

def samedigits(a,b):
  if (len(a)!=len(b)): return 0
  for i,j in zip(sorted(list(a)),sorted(list(b))):
    if (i != j): return 0
  return 1
  
x = 0
while (1):
  x += 1
  mults = (2*x, 3*x, 4*x, 5*x, 6*x)
  digs = len(str(mults[0]))
  if (all(samedigits(str(mults[i]),str(mults[i+1])) for i in xrange(4))):
    break
print x