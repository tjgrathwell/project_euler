def permutations(seq):
  if len(seq) == 1:
    yield seq
  else:
    for i in xrange(len(seq)):
      for j in [[seq[i]] + x for x in permutations(seq[:i] + seq[i+1:])]:
        yield j
    
permmaker = permutations(['0','1','2','3','4','5','6','7','8','9'])
for i in xrange(1000000):
  item = permmaker.next()
print int(''.join(item))