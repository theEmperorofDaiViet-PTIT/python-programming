isPRIME = [True] * 1000008
isPRIME[0] = isPRIME[1] = False

i = 2
while i * i <= 1000007:
	if isPRIME[i] == True:
		for j in range(i * i, 1000008, i):
			isPRIME[j] = False
	i += 1

def checkPRIME(n):
	return isPRIME[n]

def checkReversePRIME(n):
	s = str(n)[::-1]
	k = int(s)
	if n == k:
		return False
	else:
		return isPRIME[k]

def checkEMIRPNUMBER(n):
	if n < 10:
		return False
	if checkPRIME(n) == True and checkReversePRIME(n) == True:
		return True
	else:
		return False


t = int(input())
for test in range(t):
	N = int(input())
	res = []
	for i in range(N):
		if i not in res:
			k = int(str(i)[::-1])
			if checkEMIRPNUMBER(i) == True and k < N:
				res.append(i)
				res.append(k)

	for mem in res:
		print(mem, end = ' ')
	print()