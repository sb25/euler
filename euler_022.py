from utils import alpha_to_num

f = open('names.txt', 'r')
names = f.read().replace('"', '').split(',')
names.sort()

print sum([sum([alpha_to_num(letter) for letter in list(name)]) * (names.index(name) + 1) for name in names])
