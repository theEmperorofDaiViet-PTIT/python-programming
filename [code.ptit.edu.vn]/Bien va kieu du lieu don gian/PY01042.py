t = int(input())
for test in range(t):
	s = input()
	check = True
	if s[0] == '0':
		check = False
	for mem in s:
		if mem not in ['0', '1', '2']:
			check = False
			break
	if check == True:
		print("YES")
	else:
		print("NO")