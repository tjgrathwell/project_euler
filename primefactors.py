import sys
import math

primes = [2]
def is_prime(candidate):
  for prime in primes:
    if (candidate % prime) == 0:
      return 0
  primes.append(candidate)
  return candidate

super_number = 317584931803
def main():
    # parse command line options
    i = 2
    current_number = super_number
    endpoint = math.sqrt(super_number)
    while(i < endpoint):
      i += 1
      if (is_prime(i)):
        if (current_number % i) == 0:
          current_number /= i
          print "now looking for factor of " + str(current_number)
          print i
          i = 2
          continue
        
if __name__ == "__main__":
    main()