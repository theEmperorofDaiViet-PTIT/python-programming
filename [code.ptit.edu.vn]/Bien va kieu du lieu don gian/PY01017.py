test = int(input())
for test_case in range(test):
	s = input()
	l = []
	for char in s:
		if char in l or (char not in l and l == []):
			l.append(char)
		else:
			print(f"{len(l)}{l[0]}", end = '')
			l = []
			l.append(char)
	print(f"{len(l)}{l[0]}")