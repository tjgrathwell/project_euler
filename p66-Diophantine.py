import math
# diophantine eq : x*x - D*y*y = 1
    
square_hash = {1:1}
squared_hash = {1:1}

def squares():
  sqr = 1
  while True:
    if (sqr in square_hash):
      yield square_hash[sqr] 
    else:
      square_hash[sqr] = sqr*sqr
      squared_hash[square_hash[sqr]] = 1
      yield square_hash[sqr]
    sqr += 1
    
sqm = squares()
    
def find_diophantine(D):
  while True:
    for sq in squares():
      rhs = D * sq + 1
      while (rhs > max(square_hash.values())):
        sqm.next()
      if (rhs in squared_hash): # perfect square
        return int(math.sqrt(rhs)), int(math.sqrt(sq))
    
maximum = 0
for i in xrange(2,1001):
  while (i > max(square_hash.keys())):
    sqm.next()
  if (i in square_hash.values()): continue
  ans = find_diophantine(i)
  print "".join([str(ans[0]),"^2 - ",str(i),"x",str(ans[1]),"^2 = 1"])
  maximum = max(maximum,ans[0])
  
print maximum