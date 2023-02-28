res = {}


t = int(input())
text = []
for test in range(t):
	text.append(input())
i = 0
while i < t:
	res[text[i]] = 0
	for j in range(i+1, t):
		if text[j] != "":
			res[text[i]] += 1
		else:
			break
	i += res[text[i]] + 2
for key, value in res.items():
	print(f"{key}: {value}")