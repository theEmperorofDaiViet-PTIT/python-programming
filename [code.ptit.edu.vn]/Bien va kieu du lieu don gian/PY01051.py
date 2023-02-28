def Sum_digits(n):
	sum_ = 0
	while n != 0:
		sum_ = sum_ + (n % 10)
		n = n // 10
	return sum_

def check(s):
	for i in range(0,len(s)):
		if s[i] != s[len(s) - 1 - i]:
			return False
	return True

test = int(input())
for t in range(test):
	n = int(input())
	n1 = Sum_digits(n)
	s1 = str(n1)
	if n1 >= 10 and check(s1) == True:
		print("YES")
	else:
		print("NO")