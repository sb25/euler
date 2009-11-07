import math

def list_item(l, start = 0, end = 0, step = 1):
  if end:
    for i in range(int(start), int(end), int(step)):
      if i >= len(l):
        break
      else:
        yield l[i]
  else:
    for i in range(int(start), int(len(l)), int(step)):
      if i >= len(l):
        break
      else:
        yield l[i]

l = range(1, 1001*1001+1)
diagonales = []
start, end, step = 0, 0, 1
for i in range(1, int(len(l)/8) + 1):
  diagonales.extend([j for j in list_item(l, start, end + 1, step)])
  step = i * 2
  start = end + step
  end += 4 * step
print sum(diagonales)