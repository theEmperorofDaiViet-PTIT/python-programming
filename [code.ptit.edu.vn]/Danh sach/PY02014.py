isPRIME = [True] * 10001
isPRIME[0] = isPRIME[1] = False

i = 2
while i * i <= 10000:
	if isPRIME[i] == True:
		for j in range(i * i, 10001, i):
			isPRIME[j] = False
	i += 1

N = int(input())
data = list(map(int, input().split()))
maximum = 0
for mem in data:
	if isPRIME[mem] == True:
		continue
	else:
		count1 = 0
		for a in range(mem + 1, 10001):
			count1 += 1
			if isPRIME[a] == True:
				break
		count2 = 0
		for b in range(mem - 1, -1, -1):
			count2 += 1
			if isPRIME[b] == True:
				break
		maximum = max([maximum, count1, count2])
print(maximum)