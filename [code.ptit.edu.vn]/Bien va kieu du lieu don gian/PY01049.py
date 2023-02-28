PRIME = [True] * 501

PRIME[0] = PRIME[1] = False
i = 2
while i * i <= 500:
	if PRIME[i] == True:
		for j in range(i * i, 500, i):
			PRIME[j] = False
	i += 1

t = int(input())
for test in range(t):
	s = input()
	check = False
	count = 0
	for index in range(len(s)):
		if PRIME[int(s[index])] == True:
			count += 1
		if count > len(s) / 2:
			check = True
			break
	if PRIME[len(s)] == True and check == True:
		print("YES")
	else:
		print("NO")
