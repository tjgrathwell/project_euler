import math
from sets import Set
def divisors(num):
  cur = num
  result = {1:1, num:1}
  while (cur != 1):
    changed = 0
    for i in xrange(2,int(math.sqrt(cur))+1):
      if (cur % i) == 0:
        result[i] = 1
        cur /= i
        result[cur] = 1
        changed = 1
        break
      changed = 0
    if (not changed):
      result[cur]
      break
  return result.keys()
  
def factors(num):
  cur = num
  result = Set()
  result.add(num)
  while (cur != 1):
    fell = 0
    for i in xrange(2,int(math.sqrt(cur))+1):
      if (cur % i) == 0:
        result.add(i)
        cur /= i
        break
      fell = 1
    if (fell):
      result.add(cur)
      break
  return result
  
print len(factors(60).intersection(factors(5)))
# print factors(3)
# print factors(10)