t = int(input())
for test in range(t):
	line = list(map(int, input().split()))
	n = line[0]
	d = line[1]
	l = list(map(int, input().split()))
	res = []
	for i in range(d,len(l)):
		res.append(l[i])
	for i in range(0, d):
		res.append(l[i])
	for mem in res:
		print(mem, end = ' ')
	print()