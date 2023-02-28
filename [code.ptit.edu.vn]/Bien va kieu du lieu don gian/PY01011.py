test = int(input())
for t in range(test):
	s = input()
	N = int(s)
	l1 = len(s) // 2
	N1 = 10 ** l1
	for i in range(2, N1, 2):
		s1 = str(i)
		s1 = s1 + s1[::-1]
		n = int(s1)
		check = True
		for char in s1:
			if int(char) % 2 != 0:
				check = False
		if n < N and check == True:
			print(f"{n} ", end = '')
	print('')