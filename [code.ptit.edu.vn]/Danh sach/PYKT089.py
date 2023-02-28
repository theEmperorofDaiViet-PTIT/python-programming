n = int(input())
data = []
while len(data) < n:
	line = list(map(int,input().split()))
	for mem in line:
		data.append(mem)
		if len(data) == n:
			break
odd = []
even = []
for mem in data:
	if mem % 2 == 0:
		even.append(mem)
	else:
		odd.append(mem)
odd = sorted(odd, reverse = True)
even = sorted(even)
res = []
io = 0
ie = 0
for mem in data:
	if mem % 2 == 0:
		res.append(even[ie])
		ie += 1
	else:
		res.append(odd[io])
		io += 1
for mem in res:
	print(mem, end = ' ')