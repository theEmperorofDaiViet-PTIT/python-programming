t = int(input())
for test in range(t):
	N = int(input())
	S = 0
	if N % 2 == 1:
		i = 1
	else:
		i = 2
	while i <= N:
		S += 1 / i
		i += 2
	print("%.6f" %S)