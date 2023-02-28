s = input()
res = {}
i = 0
while i + 1 < len(s):
	if s[i:i+2] not in res:
		res[(s[i:i+2])] = 1
	else:
		res[(s[i:i+2])] += 1
	i += 2
for key, value in res.items():
	print(f"{key} {value}")