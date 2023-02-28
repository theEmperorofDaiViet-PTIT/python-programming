import math
def checkPRIME(n):
	if n < 2:
		return False
	if n % 2 == 0:
		if n == 2:
			return True
		else:
			return False
	for i in range(3, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

N = int(input())
l = list(map(int,input().split()))
PRIME = []
i = 0
check = []
res = [0,] * N 
for mem in l:
	if checkPRIME(mem) == True:
		PRIME.append(mem)
		check.append(True)
	else:
		res[i] = mem
		check.append(False)
	i += 1
PRIME = sorted(PRIME)
j = 0
for mem in PRIME:
	for index in range(j,len(res)):
		j += 1
		if check[j - 1] == True:
			res[j - 1] = mem
			break

for mem in res:
	print(mem, end = ' ')