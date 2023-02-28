import math
def Sum_digits(n):
	sum_ = 0
	for char in n:
		sum_ = sum_ + int(char)
	return sum_
def PRIME(n):
	if n < 2:
		return False
	if n % 2 == 0:
		if n == 2:
			return True
		else:
			return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

test = int(input())
for t in range(test):
	n = input()
	if PRIME(Sum_digits(n)) == True:
		print("YES")
	else:
		print("NO")