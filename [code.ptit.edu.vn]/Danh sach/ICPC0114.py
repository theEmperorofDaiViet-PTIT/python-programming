import math

def checkPRIME(n):
	if n < 2:
		return False
	if n % 2 == 0:
		if n == 2:
			return True
		else:
			return False
	check = True
	for i in range(3, math.ceil(math.sqrt(n)), 2):
		if n % i == 0:
			check = False
			break
	return check

def checkReversePRIME(n):
	s = str(n)[::-1]
	k = int(s)
	return checkPRIME(k)

def checkSumPRIME(n):
	s = str(n)
	k = 0
	for char in s:
		k += int(char)
	return checkPRIME(k)

def checkDigitPRIME(n):
	s = str(n)
	for char in s:
		if checkPRIME(int(char)) == False:
			return False
	return True

t = int(input())
for test in range(t):
	n = int(input())
	if checkPRIME(n) == True and checkReversePRIME(n) == True and checkSumPRIME(n) == True and checkDigitPRIME(n) == True:
		print("Yes")
	else:
		print("No")