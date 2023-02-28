import math

oo = 1000007
spf = [0 for i in range(oo+1)]

def sieve():
	spf[1] = 1
	for i in range(2, oo):
		spf[i] = i

	for i in range(4, oo, 2):
		spf[i] = 2
	for i in range(3, math.ceil(math.sqrt(oo))):
		if spf[i] == i:
			for j in range(i*i, oo, i):
				spf[j] = i

def getFactor(n):
	res = {}
	if n > oo:
		if n % 2 == 0:
			res[2] = 1
			n = int(n / 2)
		else:
			for i in range(3, math.ceil(math.sqrt(n)), 2):
				if n % i == 0:
					res[i] = 1
					n = int(n / i)
					break
	while math.abs(n) != 1:
		if spf[n] in res:
			res[spf[n]] += 1
		else:
			res[spf[n]] = 1
		n = int(n / spf[n])
	return res

sieve()
result = 0
n = int(input())
for i in range(n):
	res = getFactor(int(input()))
	for key, value in res.items():
		result += key * value
print(result)