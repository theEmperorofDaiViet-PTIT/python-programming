test = int(input())
for test_case in range(test):
	s = input()
	check = True
	for i in range(1,len(s)):
		if s[i-1] > s[i]:
			check = False
			break
	if check == True:
		print("YES")
	else:
		print("NO")
