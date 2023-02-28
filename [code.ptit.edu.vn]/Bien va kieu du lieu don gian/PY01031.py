Dict = {}
for i in range(0,10):
	Dict[i] = str(i)
tmp = 65
for i in range(10,36):
	Dict[i] = chr(tmp)
	tmp += 1
t = int(input())
for test in range(t):
	l = list(map(int, input().split()))
	N = l[0]
	b = l[1]
	res = ""
	while N != 0:
		res = Dict[N % b] + res
		N = N // b
	print(res)