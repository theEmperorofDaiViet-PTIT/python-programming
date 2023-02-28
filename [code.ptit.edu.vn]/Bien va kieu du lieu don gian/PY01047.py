PRIME = [True] * 10000
PRIME[0] = PRIME[1] = False

i = 2
while i * i < 10000:
	for j in range(i * i, 10000, i):
		PRIME[j] = False
	i += 1

t = int(input())
for test in range(t):
	s = input()
	n = int(s[-4:])
	if PRIME[n] == True:
		print("YES")
	else:
		print("NO")
