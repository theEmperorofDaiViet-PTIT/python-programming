import itertools
import math
isPRIME = [True] * 32000
PRIME = []
isPRIME[0] = isPRIME[1] = False

i = 2
while i < 32000:
	if isPRIME[i] == True:
		PRIME.append(i)
		for j in range(i*i, 32000, i):
			isPRIME[j] = False
	i += 1

N = int(input())
p = []
for mem in PRIME:
	if mem < math.floor(math.sqrt(N)):
		p.append(mem)
	else:
		break
com = itertools.combinations(p, 2)
count = 0
for mem in p:
	if mem ** 8 <= N:
		count += 1
	else:
		break
for mem in com:
	if (mem[0] * mem[1]) ** 2 <= N:
		count += 1
print(count)