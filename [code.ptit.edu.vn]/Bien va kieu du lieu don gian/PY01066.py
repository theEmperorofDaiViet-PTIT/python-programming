def check(s):
	s1 = s
	s2 = s[::-1]
	for i in range(1,len(s)):
		if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
			return False
	return True

t = int(input())
for test in range(t):
	s = input()
	if check(s) == True:
		print("YES")
	else:
		print("NO")