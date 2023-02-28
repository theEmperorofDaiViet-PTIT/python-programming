A = input().lower()
B = input().lower()

setA = set()
setB = set()

ignore = ['.', '?', ',', ' ']
for char in A:
	if char not in ignore:
		setA.add(char)
for char in B:
	if char not in ignore:
		setB.add(char)

union = setA.union(setB)
intersection = setA.intersection(setB)

a = len(union)
b = len(intersection)
if a == 0:
	res = 1
else:
	res = b / a
print("%.2f" % res)
