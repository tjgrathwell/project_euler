C = {}
def collatz(num):
  result = 1
  while(num != 1):
    if (num in C):
      return C[num] + result
    if (num%2 == 0):
      num = num/2
    else:
      num = 3*num + 1
    result += 1
  C[num] = result
  return result
  
maxlatz = 0
for i in xrange(1,1000000):
  if (i%10000 == 0): print i
  if (collatz(i) > maxlatz):
    maxlatz = collatz(i)
    starting = i
  
print starting, maxlatz