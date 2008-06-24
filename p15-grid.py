cached = {}
def paths(x,y,size):
  if ((x,y) in cached):
    return cached[(x,y)]

  if (x == size or y == size):
    return 1
  retval = paths(x+1,y,size) + paths(x,y+1,size)
  cached[(x,y)] = retval
  return retval
  
print paths(0,0,20)