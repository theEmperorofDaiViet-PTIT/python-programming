char = {}
d = 0
for c in range(ord('0'), ord('9') + 1):
	char[d] = chr(c)
	d += 1
for c in range(ord('A'), ord('Z') + 1):
	char[d] = chr(c)
	d += 1

t = int(input())
for test in range(t):
	data = list(map(int, input().split()))
	n = data[0]
	base = data[1]
	res = ""
	while n != 0:
		res = char[n % base] + res
		n = n // base
	print(res)
