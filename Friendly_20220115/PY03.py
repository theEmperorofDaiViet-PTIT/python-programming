name = set()
T = int(input())
for t in range(T):
	s = input().lower()
	name.add(s)
res = list(name)
res = sorted(res)
for mem in res:
	print(mem)