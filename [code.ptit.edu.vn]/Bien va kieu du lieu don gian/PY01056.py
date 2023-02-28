import math
def checkEVEN(s):
	index = 0;
	while index <= len(s) - 1:
		if int(s[index]) % 2 != 0:
			return False
		index += 2
	return True

def checkODD(s):
	index = 1;
	while index <= len(s) - 1:
		if int(s[index]) % 2 == 0:
			return False
		index += 2
	return True

def checkPRIME(n):
	if n < 2:
		return False
	if n % 2 == 0:
		if n == 2:
			return True
		else:
			return False
	check = True
	for i in range(3,int(math.sqrt(n))+1,2):
		if n % i == 0:
			return False
	return check

def checkSumDigits(s):
	sum_ = 0
	for digit in s:
		sum_ += int(digit)
	return checkPRIME(sum_)

t = int(input())
for test in range(t):
	s = input()
	if(checkEVEN(s) == False or checkODD(s) == False or checkSumDigits(s) == False):
		print("NO")
	else:
		print("YES")
