# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
from utils import *

print sum([i for i in xrange(2, 2000000) if isPrime(i)])