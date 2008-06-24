# Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal 	  	Pn=n(3n1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	Hn=n(2n1) 	  	1, 6, 15, 28, 45, ...

def triangle(n):
  return n*(n+1)/2
def pentagon(n):
  return n*(3*n-1)/2
def hexagon(n):
  return n*(2*n-1)

ntri = 285
npen = 165
nhex = 143

while(1):
  if (pentagon(npen) < triangle(ntri)):
    npen += 1
  elif (hexagon(nhex) < triangle(ntri)):
    nhex += 1
  else:
    ntri += 1

  if triangle(ntri) == pentagon(npen) == hexagon(nhex): break

print ntri, npen, nhex, triangle(ntri)