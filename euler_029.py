import math

l = []
for a in range(2, 101):
  for b in range(2, 101):
    nb = math.pow(a, b)
    if not nb in l:
      l.append(nb)
print len(l)