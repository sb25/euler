# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome = ""
for i in range(999,99,-1):
  for j in range(i,99,-1):
    s = str(i * j)
    first_part = list(s[:len(s)/2])
    last_part = list(s[len(s)/2:])
    last_part.reverse()
    if first_part == last_part:
      if s > palindrome:
        palindrome = s
print palindrome
