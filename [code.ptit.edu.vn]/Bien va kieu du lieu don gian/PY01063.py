t = int(input())
for test in range(t):
	s = input()
	n = input()
	count = 0
	i = 0
	while i < len(s):
		index = s.find(n, i)
		if index != -1:
			count += 1
			i = index + len(n)
		else:
			i += 1
	print(count)