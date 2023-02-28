import math
def gcd(a, b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a

def PRIME(n):
	if n < 2:
		return False
	if n % 2 == 0:
		if n == 2:
			return True
		else:
			return False
	for i in range(3,n,2):
		if n % i == 0:
			return False
	return True

test = int(input())
for test_case in range(test):
	numbers = list(map(int,input().split()))
	a = numbers[0]
	b = numbers[1]
	c = gcd(a,b)
	summ = 0
	while c > 0:
		summ = summ + int(c % 10)
		c = int(c / 10)
	# print(type(summ))
	if PRIME(summ) == True:
		print("YES")
	else:
		print("NO")
