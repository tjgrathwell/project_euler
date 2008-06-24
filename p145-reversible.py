import time
import math

these_is = {}
these_aint = {}
def is_reversible(num):
  if(num in these_is):
    del these_is[num]
    return 1
  if(num in these_aint):
    del these_aint[num]
    return 0

  # no leading zeroes allowed in reversed version
  if (num[-1] == '0'): return 0

  reverse = str(int(num[::-1]))
  sum = int(num) + int(reverse)
  if ((sum % 2) == 0):
    these_aint[reverse] = 1
    return 0
  elif any(e in str(sum)[:-1] for e in ['0','2','4','6','8']):
    these_aint[reverse] = 1
    return 0
  else:
    these_is[reverse] = 1
    return 1

def main():
  start = time.time()
  print len([x for x in xrange(1,10**6) if is_reversible(str(x))])
  print "Took " + str(time.time() - start) + " seconds"

if __name__ == '__main__':
    main()