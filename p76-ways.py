saved_ways = {1:[[1]]}
def ways(n):
  if n in saved_ways:
    return saved_ways[n]

  result = []
  for i in xrange(1,n):
    for newway in [[i] + way for way in ways(n-i)]:
      result.append(newway)
  result.append([n])
  return result
  
print ways(4)

#naive and incomplete