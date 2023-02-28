test = int(input())
for test_case in range(test):
	s = input()
	check = True
	for digit in s:
		if digit != '4' and digit != '7':
			check = False
			break
	if check == True:
		print("YES")
	else:
		print("NO")