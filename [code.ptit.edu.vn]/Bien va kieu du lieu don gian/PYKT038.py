def convert(s):
	if len(s) < 3:
		while len(s) < 3:
			s = "0" + s
	res = int(s[0]) * (2 ** 2) + int(s[1]) * 2 + int(s[2])
	return str(res)

n = input()[::-1]
res = ""
for start in range(0, len(n), 3):
	res = convert((n[start:start+3])[::-1]) + res
print(res)