pentagons = {}
pent_vals = {}
class S:
  max_n, max_pent = 0, 0

def pentagon(n):
  if (n not in pentagons):
    pentagons[n] = n*(3*n-1)/2
    pent_vals[n*(3*n-1)/2] = 1
    if (pentagons[n] > S.max_pent):
      S.max_n, S.max_pent = n, pentagons[n]
  return pentagons[n]
  
def is_pent(candidate):
  while (candidate > S.max_pent):
    pentagon(S.max_n + 1)
  if (candidate in pent_vals):
    return 1
  return 0
  
i = 1
j = 1
while 1:
  if (is_pent(pentagon(i)-pentagon(j))):
    if (is_pent(pentagon(i)+pentagon(j))):
      print i, j, abs(pentagon(i)-pentagon(j))
  if (i == j):
    i += 1
    j = 1
  else:
    j += 1
    
# solution 5482660. This solution sucks though, it takes like a minute and seems to find it by accident. Other people say they can get subsecond response.