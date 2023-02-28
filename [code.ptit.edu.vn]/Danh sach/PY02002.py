test = int(input())
for test_case in range(test):
	numbers = list(map(int, input().split()))
	s = numbers[0]
	e = numbers[1]
	if e > s and s >= 1:
		order = 3
		a = 1
		b = 1
		if s == 1:
			print(f"{a} {b} ", end = '')
		elif s == 2:
			print(f"{b} ", end = '')
		while True:
			temp = b
			b = a + b
			a = temp
			if(order >= s):
				print(f"{b} ", end = '')
			if(order == e):
				break
			order += 1
		print("")
	else:
		continue
