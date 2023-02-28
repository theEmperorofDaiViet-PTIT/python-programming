import math

def checkKRISH(n):
	s = str(n)
	summ = 0
	for char in s:
		summ += math.factorial(int(char))
	if summ == n:
		return True
	else:
		return False


t = int(input())
for test in range(t):
	n = int(input())
	if checkKRISH(n) == True:
		print("Yes")
	else:
		print("No")