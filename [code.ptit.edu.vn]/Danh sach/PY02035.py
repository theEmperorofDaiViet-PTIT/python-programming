s = input()
k = int(input())
res = {}
i = 0
while i + 1 < len(s):
	if s[i:i+2] not in res:
		res[(s[i:i+2])] = 1
	else:
		res[(s[i:i+2])] += 1
	i += 2
found = False
for key, value in sorted(res.items()):
	if value >= k:
		found = True
		print(f"{key} {value}")
if found == False:
	print("NOT FOUND")