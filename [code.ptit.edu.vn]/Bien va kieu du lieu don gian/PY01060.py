def sumOfODD(s):
	sum_ = 0
	index = 1
	while index < len(s):
		sum_ += int(s[index])
		index += 2
	return sum_

def mulOfEVEN(s):
	checkAllZero = True
	mul = 1
	index = 0
	while index < len(s):
		if s[index] != '0':
			checkAllZero = False
			mul *= int(s[index])
		index += 2
	if checkAllZero == True:
		return 0
	else:
		return mul

t = int(input())
for test in range(t):
	s = input()
	print(mulOfEVEN(s), end = ' ')
	print(sumOfODD(s))