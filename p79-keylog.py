attempts = [line.strip() for line in open("keylog.txt")]

shortest = attempts[0]
def find_shortest(lhs,rhs):
  pos = 0
  for i,c in enumerate(rhs):
    for j,d in enumerate(lhs[pos:]):
      missed = 1
      if (c==d):
        missed = 0
        pos = pos+j+1
        break
    if missed:
      lhs = lhs + rhs[i:]
      break
  return lhs

record = [attempts[0]]
for a in attempts[1:3]:
  print "attempt: ", a
  next = []
  for item in record:
    one = find_shortest(item,a)
    two = find_shortest(a,item)
    print "one, two: ", one, two
    next.append(one)
    next.append(two)
  record = next

print record