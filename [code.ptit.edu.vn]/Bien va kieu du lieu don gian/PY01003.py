test = int(input())
def Round_number(n,l):
	mul = 10
	for loop in range(l):
		n = int((n / mul) + 0.5) * mul
		mul *= 10
	return n

for t in range(test):
	s = input()
	n = int(s)
	if n <= 10:
		print(n)
	else:
		l = len(s) - 1
		print(Round_number(n,l))
