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
	if checkPRIME(len(s)) == False:
		return False
	count = 0;
	for digit in s:
		if checkPRIME(int(digit)) == True:
			count += 1
	if count <= len(s) - count:
		return False
	return True

t = int(input())
for test in range(t):
	s = input()
	if Qualifiers(s) == True:
		print("YES")
	else:
		print("NO")
