t = int(input())
for test in range(t):
	data = list(map(int, input().split()))
	N = data[0]
	K = data[1]

	s = "A"
	index = ord("A")
	count = 1
	while count < N:
		count += 1
		index += 1
		s = s + str(chr(index)) + s
	print(s[K-1])