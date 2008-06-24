def binary(n):
  result = []
  while n:
    result.append(n&1)
    n >>= 1
  return result

# binary = lambda n: n>0 and [n&1]+binary(n>>1) or []

def is_palindrome(candidate):
  for i in xrange(len(candidate) / 2):
    if (candidate[i] != candidate[-i - 1]):
      return 0
  return 1

winners = []
  
for i in xrange(1,1000):
  if (i % 10000 == 0): print i
  if is_palindrome( binary( int(str(i) + str(i)[::-1]) ) ):
    winners.append(int(str(i) + str(i)[::-1]))
  if is_palindrome( binary( int(str(i) + str(i)[:-1][::-1]) ) ):
    winners.append(int(str(i) + str(i)[:-1][::-1]))
  
print winners
print sum(winners)

# [1, 33, 3, 5, 7, 99, 9, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 585585, 73737, 13500531, 1758571, 1934391, 1979791, 3129213, 5071705, 5259525, 5841485, 1290880921, 719848917, 7451111547L, 910373019, 939474939, 10050905001L, 110948849011L, 136525525631L, 18462126481L, 32479297423L, 75015151057L]
# 394832891346