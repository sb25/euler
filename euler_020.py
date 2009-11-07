# coding: utf8
# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# Find the sum of the digits in the number 100!

print sum(map(int, list(str(eval("*".join(map(str, range(1,101))))))))