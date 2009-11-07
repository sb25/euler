from utils import permutation

permutations = [p for p in permutation("0123456789")]
permutations.sort()
print permutations[999999]