t = int(input())
for test in range(t):
	data = list(map(int, input().split()))
	n = data[0]
	m = data[1]
	l = list(map(int, input().split()))

	maximum = max(l)
	index = l.index(maximum)
	l1 = []
	for i in range(0, index):
		l1.append(l[i])
	l1.append(m)
	for i in range(index, len(l)):
		l1.append(l[i])

	negative = []
	positive = []
	for mem in l1:
		if mem < 0:
			negative.append(mem)
		else:
			positive.append(mem)
	for mem in negative:
		print(mem, end = ' ')
	for mem in positive:
		print(mem, end = ' ')
	print()