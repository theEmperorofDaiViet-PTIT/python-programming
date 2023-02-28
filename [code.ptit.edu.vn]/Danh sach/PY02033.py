s = input()
res = []
i = 0
while i + 1 < len(s):
	if s[i:i+2] not in res:
		res.append(s[i:i+2])
	i += 2
for mem in res:
	print(mem, end = ' ')