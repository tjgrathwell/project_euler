import sieve, sys
class G:
  s = sieve.eratosthenes()
  lastprime = s.next()
  
def spiral_diag():
  last = 1
  stepsize = 2
  while 1:
    this_term = []
    for i in xrange(4):
      last += stepsize
      this_term.append(last)
    stepsize += 2
    yield this_term

# def make_primes(number):
  # for i in xrange(number):
    # G.primes.append(G.s.next())
  
def check_diag(diag):
  result = 0
  for n in diag:
    while n > G.lastprime:
      G.lastprime = G.s.next()
    if n == G.lastprime:
      result += 1
  return result
  
def main():
  diag = spiral_diag()
  num_diag = 1
  total_primes = 0
  while(1):
    this_diag = diag.next()
    num_diag += 4
    total_primes += check_diag(this_diag)
    density = total_primes / float(num_diag)
    print num_diag, total_primes, density
    if density < .1:
      print "side length: " + str(((num_diag-1)/4) * 2 - 1)
      sys.exit(1)
    
if __name__ == "__main__":
  import psyco
  main()