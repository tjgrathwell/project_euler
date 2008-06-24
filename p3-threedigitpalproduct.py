def is_palindrome(candidate):
  for i in xrange(len(candidate) / 2):
    if (candidate[i] != candidate[-i - 1]):
      return 0
  return 1  

biggest = 0
for i in xrange(1,999):
  for j in xrange(1,999):
    if (is_palindrome(str(i*j))):
      if (i * j) > biggest:
        biggest = i * j
        print biggest