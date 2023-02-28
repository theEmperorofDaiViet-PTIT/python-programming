import itertools

data = list(map(int, input().split()))
N = data[0]
K = data[1]
name = list(set(list(input().split())))
for mem in itertools.combinations(sorted(name), K):
	for member in mem:
		print(member, end = ' ')
	print()