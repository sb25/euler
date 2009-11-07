# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^(2) + b^(2) = c^(2)
# 
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def main():
  for a in range(1,999):
    for b in range(2,999):
      c = 1000 - b - a
      a2 = math.pow(a,2)
      b2 = math.pow(b,2)
      c2 = math.pow(c,2)
      if a2 + b2 == c2:
        return a*b*c

print main()