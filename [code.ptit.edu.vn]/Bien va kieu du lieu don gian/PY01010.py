test = int(input())
for test_case in range(test):
	s = input()
	if len(s) >= 4:
		if s[0] == s[-2] and s[1] == s[-1]:
			print("YES")
		else:
			print("NO")