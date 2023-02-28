def GCD(a,b):
	while b != 0:
		tmp = b
		b = a % b
		a = tmp
	return a

t = int(input())
for test in range(t):
	s1 = input()
	s2 = s1[::-1]
	n1 = int(s1)
	n2 = int(s2)
	if GCD(n1,n2) == 1:
		print("YES")
	else:
		print("NO")