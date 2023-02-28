import itertools
data1 = list(map(int, input().split()))
N = data1[0]
K = data1[1]
data2 = list(map(int, input().split()))
s = set(data2)
l = sorted(list(s))

for com in itertools.combinations(l, K):
	for mem in com:
		print(mem, end = ' ')
	print()