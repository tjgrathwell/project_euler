import math

# this code does WAY TOO MUCH WORK for what it is.
# but I think the algorithm is fun.

def is_prime(candidate):
  for i in xrange(2,int(math.ceil(math.sqrt(candidate)))):
    if (candidate % i) == 0:
      return 0
  return 1

def triangle():
  sum = 0
  base = 1
  while(1):
    sum += base
    yield sum
    base += 1

DIVISORS = {2 : [1,2], 4 : [1,2,4]}
def divisors(num):
  if (DIVISORS.has_key(num)):
    return DIVISORS[num]

  if (is_prime(num)):
    DIVISORS[num] = [1,num]
    return DIVISORS[num]
    
  for i in xrange(2,int(math.ceil(math.sqrt(num)))):
    if (num%i == 0):
      smaller = num/i
      DIVISORS[num] = cross_union(divisors(i), divisors(smaller))
      return DIVISORS[num]
    
def cross_union(a,b):
  result = [] 
  for a_item in a:
    for b_item in b:
      mult = a_item * b_item
      if (mult not in result):
        result.append(mult)
  result.sort()
  return result


i = 0
trigen = triangle()
while(1):
  i = trigen.next()
  divis = divisors(i)
  print i, len(divis)
  if (len(divis) > 500):
    print i, divis
    exit(1)