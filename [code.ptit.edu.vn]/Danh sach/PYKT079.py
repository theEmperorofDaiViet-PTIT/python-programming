t = int(input())
for test in range(t):
	amount = int(input())
	l = list(map(int, input().split()))
	minimum = min(l)
	maximum = max(l)
	set1 = set([x for x in range(minimum, maximum + 1)])
	set2 = set(l)
	print(len(set1) - len(set2))