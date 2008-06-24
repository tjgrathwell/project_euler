import sys, getopt
def usage():
  print "usage: " + sys.argv[1] + "[--verbose] filename" 
  exit(1)

try:
  optlist, args = getopt.getopt(sys.argv[1:],"",["verbose"])
except getopt.GetoptError:
  usage()

if not len(args):
  usage()

VERBOSE = 1 if (any(opt[0] == '--verbose' for opt in optlist)) else 0
  
file = open(args[0],"r")
dataset = []
for line in file:
  dataset.append([int(num) for num in line.split(" ")]) 

def reduce_triangle(triangle):
  if (len(triangle) < 2): return 0

  for i in xrange(len(triangle[-1])-1):
    triangle[-2][i] += max(triangle[-1][i], triangle[-1][i+1])
  triangle.pop()
  return 1
  
if (VERBOSE): print dataset
while reduce_triangle(dataset):
  if (VERBOSE): print dataset
print dataset