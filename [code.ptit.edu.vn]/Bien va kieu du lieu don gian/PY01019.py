test = int(input())
for test_case in range(test):
	s = input()
	rs = s [::-1]
	check = True
	i = 1
	for char in s[1:]:
		if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rs[i]) - ord(rs[i-1])):
			check = False
			break
		i += 1
	if check == True:
		print("YES")
	else:
		print("NO")