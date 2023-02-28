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

t = int(input())
for test in range(t):
	s = input()
	if checkPRIME(int(s[-3:])) == True and checkPRIME(int(s[:3])):
		print("YES")
	else:
		print("NO")