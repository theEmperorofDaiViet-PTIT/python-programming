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
	for i in range(3,int(math.sqrt(n))+1,2):
		if n % i == 0:
			return False
	return check

def Qualifiers(s):
	index = 0
	while index < len(s):
		if checkPRIME(index) == True and checkPRIME(int(s[index])) != True:
			return False
		if checkPRIME(index) == False and checkPRIME(int(s[index])) != False:
			return False
		index += 1
	return True

t = int(input())
for test in range(t):
	s = input()
	if Qualifiers(s) == True:
		print("YES")
	else:
		print("NO")