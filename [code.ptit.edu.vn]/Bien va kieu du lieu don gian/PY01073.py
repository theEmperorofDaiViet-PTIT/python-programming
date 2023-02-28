import itertools
s = input()
for per in itertools.permutations(s):
	res = "".join(per)
	print(res)