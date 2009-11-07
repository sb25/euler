import math, sys

def get_divisors(nb, known_divisors = {1 : [1]}):
  if nb in known_divisors.keys():
    return known_divisors
  
  known_divisors[nb] = []
  for i in range(nb, 0, -1):
    if nb%i == 0:
      divisors = get_divisors(i, known_divisors)
      for divisor in divisors[i]:
        if not divisor in known_divisors[nb]:
          known_divisors[nb].append(divisor)
  known_divisors[nb].append(nb)
  known_divisors[nb].sort()
  return known_divisors

def alpha_to_num(alpha):
  dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return dic.index(alpha.upper()) + 1

def isPrime(nb):
  if nb < 2:
    return False
    
  if nb == 2:
    return True
  
  if nb%2 == 0:
    return False
    
  for x in xrange(3, int(math.sqrt(nb)) + 1, 2):
    if nb%x == 0:
      return False
  return True
  
def factorize(nb):
  primes = []
  candidates = xrange(2,nb+1)
  candidate = 2
  while not primes and candidate in candidates:
    if nb%candidate == 0 and isPrime(candidate):
      if not candidate in primes:
        primes.append(candidate)
      for prime in factorize(nb/candidate):
        if not prime in primes:
          primes.append(prime)
    candidate += 1
  return primes
  
def primes(n):
  """
  Yield all primes below number n
  """
  sieve = [True]*(n+1)
  for i in xrange(2, n+1):
    if sieve[i]:
      yield i
      for j in xrange(2*i, n+1, i): sieve[j] = False

def get_primes_below(n):
  """
  Return all primes below number n as a list
  """
  return [p for p in primes(n)]

def permutation(L):
  if len(L) <=1:
    yield L
  else:
    for perm in permutation(L[1:]):
      for i in range(len(perm)+1):
        yield perm[:i] + L[0:1] + perm[i:]

def PGCD(a, b):
  if b > a:
    a, b = b, a
    
  r = a%b
  if r:
    return PGCD(b, r)
  return b
  
def PPCM(a, b):
  return (a * b)/PGCD(a, b)
