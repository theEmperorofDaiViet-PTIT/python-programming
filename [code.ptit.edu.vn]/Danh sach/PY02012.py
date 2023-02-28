N = int(input())
l = []
l_check = []
l_odd = []
l_even = []
while N > 0:
	line = list(map(int,input().split()))
	for mem in line:
		l.append(mem)
		N -= 1
		if mem % 2 == 0:
			l_even.append(mem)
			l_check.append(False)
		else:
			l_odd.append(mem)
			l_check.append(True)
		if N == 0:
			break
l_even = sorted(l_even)
l_odd = sorted(l_odd, reverse = True)
i_odd = 0
i_even = 0
for i in range(len(l)):
	if l_check[i] == False:
		print(l_even[i_even], end = ' ')
		i_even += 1
	elif l_check[i] == True:
		print(l_odd[i_odd], end = ' ')
		i_odd += 1