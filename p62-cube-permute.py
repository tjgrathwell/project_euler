import math
# diophantine eq : x*x - D*y*y = 1
    
def permutations(seq):
  if len(seq) == 1:
    yield seq
  else:
    for i in xrange(len(seq)):
      for j in [[seq[i]] + x for x in permutations(seq[:i] + seq[i+1:])]:
        yield j
        
def is_perm(a,b):
    a_hash = {}
    for c in str(a):
        a_hash[c] = 1 if c not in a_hash else a_hash[c] + 1
    for c in str(b):
        if c in a_hash and a_hash[c]:
            a_hash[c] -= 1
        else:
            return False
    return True
    
cubes = []
lengths = []
first_length = {}
def add_cube():
    cube = len(cubes)**3
    cubes.append(cube)
    cube_length = len(str(cube))
    lengths.append(cube_length)
    if cube_length not in first_length:
        first_length[cube_length] = len(cubes)-1
n = 0    
while True:
    # if we haven't made the cube for this iteration yet, make it
    if len(cubes) <= n:
        add_cube()
    this_cube = cubes[n]
    this_cube_length = lengths[n]

    # if we haven't generated all the cubes the same size as this cube, make more
    while lengths[-1] <= this_cube_length:
        add_cube()

    result = [n]
    slice_start = first_length[this_cube_length]
    for i,c in enumerate(cubes[slice_start:]):
        if c != this_cube and lengths[slice_start+i] == this_cube_length and is_perm(c, this_cube):
            result.append(slice_start+i)
    if len(result) > 4:
        print [(r,r**3) for r in result]

    n += 1
    
# a useful fix here instead of 'is_perm' is to sort the digits of each number and use that as a 'canonical representation' - two numbers with the same sorted digits hashed end up being the same thing