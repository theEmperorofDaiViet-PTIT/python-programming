def Try(n, A, B, C):
	if n == 1:
		print(f"{A} -> {C}")
		return 0
	else:
		Try(n-1, A, C, B)
		Try(1, A, B, C)
		Try(n-1, B, A, C)

a = "A"
b = "B"
c = "C"
n = int(input())
Try(n, a, b, c)