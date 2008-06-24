# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# (1) .. 2 (3) 4 (5) 6 (7) 8 (9)..  10 11 12 (13) 14 15 16 (17) 18 19 20 (21) 22 23 24 (25) .. 26 27 28 29 30 (31)
# period keeps increasing by 2 in sets of four

def spiral_diag(terms):
  result = [1]
  last = 1
  stepsize = 2
  while len(result) < terms:
    for i in xrange(4):
      last += stepsize
      result.append(last)
    stepsize += 2
  return result
    
# 1x1 spiral has one term. 3x3 has five. 5x5 has nine. 1001x1001 has 1+4*500 = 2001
print sum(spiral_diag(2001))