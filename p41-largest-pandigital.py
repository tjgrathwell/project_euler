# From forumgoers smarte than I:

# Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
# Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3) 

from rabin_miller import rabin_miller

def swap(l, a, b):
  temp = l[a];
  l[a] = l[b];
  l[b] = temp; 

# "SEPA algorithm" per a forums answer to p24
def permute(str,len):
  key = len-1
  newkey = len-1
  while ((key > 0) and (str[key] >= str[key-1])):
    key -= 1
  key -= 1
  if (key < 0):
    return 0
  newkey = len-1
  while ((newkey > key) and (str[newkey] >= str[key])):
    newkey -= 1
  swap(str,key,newkey)
  len -= 1
  key += 1
  while(len>key):
    swap(str,len,key)
    key += 1
    len -= 1
  return 1

def permutations(seq):
  if len(seq) == 1:
    yield seq
  else:
    for i in xrange(len(seq)):
      for j in [[seq[i]] + x for x in permutations(seq[:i] + seq[i+1:])]:
        yield j
    
# try all # of digits counting down from 7
    
digits = range(1,8)
digits.reverse()
for d in digits:
    # iterate through permutations in reverse numerical order
    for l in [[str(c) for c in range(1,d)]]:
        found = False
        l.reverse()
        lenl = len(l)
        print l
        while permute(l,lenl):
          il = int(''.join(l))
          if rabin_miller(il):
            print il
            found = True
            break
    if found:
        break