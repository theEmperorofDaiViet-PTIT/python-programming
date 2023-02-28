data1 = input().lower()
data2 = input().lower()

dat1 = data1.split("/t")
dat2 = data2.split("/t")

l1 = []
l2 = []

for mem in dat1:
	tmp = mem.split()
	for member in tmp:
		l1.append(member)

for mem in dat2:
	tmp = mem.split()
	for member in tmp:
		l2.append(member)

set1 = set(l1)
set2 = set(l2)

inter = set1.intersection(set2)
union = set1.union(set2)



for mem in sorted(list(union)):
	print(mem, end = ' ')
print()
for mem in sorted(list(inter)):
	print(mem, end = ' ')