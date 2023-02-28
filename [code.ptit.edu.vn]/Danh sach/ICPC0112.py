oo = 1000000
isPRIME = [True] * (oo + 1)
isPRIME[0] = isPRIME[1] = False
PRIME = []
i = 2
while i * i < oo:
	if isPRIME[i] == True:
		PRIME.append(i)
		for j in range(i * i, oo + 1, i):
			isPRIME[j] = False		
	i += 1

def count(N):
	res = 0
	for mem in PRIME:
		if mem >= N - 6:
			break
		if (mem + 2) in PRIME and (mem + 6) in PRIME:
			res += 1
		if (mem + 4) in PRIME and (mem + 6) in PRIME:
			res += 1
	return res

t = int(input())
for test in range(t):
	N = int(input())
	print(count(N))
