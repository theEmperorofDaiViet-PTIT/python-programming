t = int(input())
res = []
for test in range(t):
	s = input()
	if s not in res:
		res.append(s)
print(len(res))