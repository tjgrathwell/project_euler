import math

def triplets():
  i = 1
  j = 1
  while(1):
    k = i*i + j*j
    sqk = math.sqrt(k)
    if (int(sqk)*int(sqk) == k):
      yield i, j, int(sqk)
    if (i == j):
      i += 1
      j = 1
    else:
      j += 1

tripmaker = triplets()
while 1:
  a,b,c = tripmaker.next()
  if ((a+b+c) == 1000):
    print a*b*c
    break