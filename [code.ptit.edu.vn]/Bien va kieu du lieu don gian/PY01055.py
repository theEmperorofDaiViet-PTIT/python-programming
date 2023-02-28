def check(s):
	if len(s) % 2 == 0:
		return False
	if s[0] == s[1]:
		return False
	index = 2;
	while(index <= len(s) - 1):
		if s[index] != s[index - 2]:
			return False
		index += 2
	return True

t = int(input())
for test in range(t):
	s = input()
	if check(s) == True:
		print("YES")
	else:
		print("NO")
