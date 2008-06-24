def is_pal(candidate):
  for i in xrange(len(candidate)/2):
    if (candidate[i] != candidate[-1 * i - 1]):
      return 0
  return 1

canpals = {}
neverpals = {}
def can_pal(num):
  friends = [num]
  current = num
  for i in xrange(50):
    current = current + int(str(current)[::-1])
    
    if current in neverpals:
      break
    
    if (current in canpals) or is_pal(str(current)):
      for n in friends:
        canpals[n] = 1
      return 1
      
    friends.append(current)
  for n in friends:
    neverpals[n] = 1
  return 0
  
lychrels = [i for i in xrange(10000) if not can_pal(i)]
print len(lychrels)