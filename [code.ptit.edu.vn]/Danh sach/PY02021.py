t = int(input())
for test in range(t):
	amount = list(map(int,input().split()))
	n1 = amount[0]
	n2 = amount[1]
	n3 = amount[2]
	l1 = list(map(int,input().split()))
	l2 = list(map(int,input().split()))
	l3 = list(map(int,input().split()))
	i, j, k = 0, 0, 0
	res = []
	while i < n1 and j < n2 and k < n3:
		if l1[i] == l2[j] and l1[i] == l3[k]:
			res.append(l1[i])
			i += 1
			j += 1
			k += 1
			continue
		if l1[i] < l2[j] or l1[i] < l3[k]:
			i += 1
			continue
		if l2[j] < l1[i] or l2[j] < l3[k]:
			j += 1
			continue
		if l3[k] < l1[i] or l3[k] < l2[j]:
			k += 1
			continue
	if len(res) == 0:
		print("NO")
	else:
		for mem in res:
			print(f"{mem} ", end = '')
		print("")
