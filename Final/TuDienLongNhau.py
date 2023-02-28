data = input().split()
N = int(data[0])
K = int(data[1])
if N > 70 or K > 5:
	print("INVALID INPUT")
else:
	dic = {}
	for n in range(N):
		a, b = input().split()
		dic[a] = int(b)
	dic = sorted(dic.items(), key = lambda k: (-k[1], k[0]))
	for k in range(K):
		print(dic[k][0], end = ' ')