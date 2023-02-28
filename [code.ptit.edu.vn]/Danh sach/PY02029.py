N, M = [int(x) for x in input().split()]
vote = [int(x) for x in input().split()]
res = {}
for mem in vote:
	if mem not in res:
		res[mem] = 1
	else:
		res[mem] += 1
maximum = 0
for value in res.values():
	if value > maximum:
		maximum = value
max2 = 0
winner = 0
found = False
for key, value in res.items():
	if value > max2 and value < maximum:
		max2 = value
		winner = key
		found = True
if found == True:
	print(winner)
else:
	print("NONE")