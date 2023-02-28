t = int(input())
for test in range(t):
	n  = int(input())
	if n % 7 == 0:
		print(n)
		continue
	count = 0
	found = False
	while count <= 1000:
		count += 1
		n += int(str(n)[::-1])
		if n % 7 == 0:
			print(n)
			found = True
			break
	if found == False:
		print(-1)