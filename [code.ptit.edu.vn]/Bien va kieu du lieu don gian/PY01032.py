data = list(map(int,input().split()))
a = int(data[0])
b = int(data[1])
M = int(data[2])

count = 0
res = [0, 1, 6643, 1422773, 5415589, 90396755477]
if M == 2:
	for i in range(a, b+1):
		tmp = bin(i)[2:]
		if tmp == tmp[::-1]:
			count += 1

if M > 2:	
	for i in range(a, b+1):
		if i in res:
			count += 1
print(count)