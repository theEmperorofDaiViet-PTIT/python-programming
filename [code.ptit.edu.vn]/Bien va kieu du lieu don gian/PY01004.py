import math
def gcd(a, b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a

def PRIME_together(a,b):
	if gcd(a,b) == 1:
		return True
	return False

def PRIME(a):
	if a < 2:
		return False
	if a % 2 == 0:
		if a == 2:
			return True
		else:
			return False
	for i in range(3,math.sqrt(a)+1,2):
		if a % i == 0:
			return False
	return True

test = int(input())
for test_case in range(test):
	n = int(input())
	count = 0
	for i in range(1,n):
		if PRIME_together(i,n) == True:
			count += 1
	if PRIME(count) == True:
		print("YES")
	else:
		print("NO")
	

