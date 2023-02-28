t = int(input())
for test in range(t):
	s = input()
	num = []
	i = 0
	while i < len(s):
		if s[i].isnumeric() == True:
			tmp = s[i]
			j = i + 1
			while j < len(s):
				if s[j].isnumeric() == True:
					tmp += s[j]
					j += 1
				else:
					break
			num.append(int(tmp))
			i = j
		else:
			i += 1
	num = sorted(num, reverse = True)
	print(num[0])