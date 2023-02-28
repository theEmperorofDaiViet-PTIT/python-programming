while True:
	n = int(input())
	if n == 0:
		break
	count = 1
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = n * 3 + 1
		count += 1
	print(count)