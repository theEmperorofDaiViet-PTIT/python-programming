import math

def sieve(n, prime, primesquare, a):
	for i in range(2,n + 1):
		prime[i] = True
	for i in range((n * n + 1) + 1):
		primesquare[i] = False
	prime[0] = prime[1] = False

	for i in range(2, math.ceil(math.sqrt(n))):
		if prime[i] == True:
			for j in range(i * i, n + 1, i):
				prime[j] = False

	j = 0
	for i in range(2,n+1):
		if prime[i] == True:
			a[j] = i
			primesquare[i * i] = True
			j += 1

def countDivisors(n):
	if n == 1:
		return 1

	prime = [False] * (n + 2)
	primesquare = [False] * ((n * n) + 2)
	a = [0] * (n + 1)

	sieve(n, prime, primesquare, a)
	count = 1

	i = 0
	while a[i] ** 3 <= n:
		cnt = 0
		while n % a[i] == 0:
			n = int(n / a[i])
			cnt += 1
		count = count * (cnt + 1)
		i += 1

	if prime[n] == True:
		count = count * 2
	elif primesquare[n] == True:
		count = count * 3
	elif n != 1:
		count = count * 2 * 2

	return count

t = int(input())
for test in range(t):
	X = int(input())
	maxCount = 0
	for i in range(1, X):
		if maxCount < countDivisors(i):
			maxCount = countDivisors(i)
	n = X
	while True:
		if countDivisors(n) > maxCount:
			print(n)
			break
		n += 1



