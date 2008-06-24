import sys

primes = [2]
def is_prime(candidate):
  for prime in primes:
    if (candidate % prime) == 0:
      return 0
  primes.append(candidate)
  return candidate

def main():
    # parse command line options
    primes_to_go = int(sys.argv[1])
    primes_to_go -= 1
    i = 2
    while(primes_to_go):
      i += 1
      if (is_prime(i)):
        primes_to_go -= 1
    print i
        
if __name__ == "__main__":
    main()