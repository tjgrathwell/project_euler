def score(position, contestant):
  return (position+1) * sum([ord(c) - 64 for c in contestant])

nameline = open("names.txt","r").readlines()[0]
names = [name[1:-1] for name in nameline.split(',')]
names.sort()

total = 0
for i, name in enumerate(names):
  total += score(i,name)
print total