get = input().split()
a = int(get[0])
K = int(get[1])
N = int(get[2])
count = 0
start = (int(a / K) + 1) * K
for j in range(start, N + 1, K):
	print(f"{j - a} ", end = '')
	count += 1
if count == 0:
	print(-1)
else:
	print('')