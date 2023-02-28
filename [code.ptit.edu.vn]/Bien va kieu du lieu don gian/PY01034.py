t = int(input())
for test in range(t):
	l = input()
	s = []
	for char in l:
		s.append(char)
	i = len(s) - 2
	while i >= 0 and s[i] <= s[i+1]:
		i -= 1
	check = True
	if i >= 0:
		j = len(s) - 1
		while j > i and s[i] <= s[j]:
			j -= 1
		k = j - 1
		while k >= 0 and s[k] == s[j]:
			j = k
			k -= 1
		if s[j] == '0' and i == 0:
			check = False
		tmp = s[i]
		s[i] = s[j]
		s[j] = tmp
	else:
		check = False
	if check == True:
		for mem in s:
			print(mem, end = '')
		print()
	else:
		print(-1)


