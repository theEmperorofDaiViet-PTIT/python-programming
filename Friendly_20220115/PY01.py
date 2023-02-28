import math

oo = 1000007
spf = [0] * (oo + 1)
spf[1] = 1

for i in range(2, oo + 1):
	spf[i] = i
for i in range(4, oo + 1, 2):
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
			for i in range(3, math.ceil(math.sqrt(n))):
				if n % i == 0:
					res[i] = 1
					n = int(n / i)
					break
					
	while abs(n) != 1:
		if spf[n] in res:
			res[spf[n]] += 1
		else:
			res[spf[n]] = 1
		n = int(n / spf[n])
	return res

res = 1
N = int(input())
for i in range(N):
	n = int(input())
	tmp = getFactor(n)
	tmpres = 0
	for key, value in tmp.items():
		tmpres += key * value
	res *= tmpres
print(res)