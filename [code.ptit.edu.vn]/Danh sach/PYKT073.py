def identify(l):
	if len(l.split()) == 6:
		return 1
	else:
		return 2

def endOfSixEight(line):
	if len(line.split()) == 7:
		return True
	else:
		return False

amount = int(input())
text = []
total = 0
res = []
for i in range(amount):
	text.append(input())
i = 0
while i < amount:
	total += 1
	form = identify(text[i])
	res.append(form)
	if form == 1:
		i += 2
		while i < amount:
			if len(text[i].split()) == 6:
				i += 2
			else:
				break
	if form == 2:
		i += 4

print(total)
for result in res:
	print(result)