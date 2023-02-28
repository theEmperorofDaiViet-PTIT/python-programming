test = int(input())
for test_case in range(test):
	s = input()
	check = True
	i = 0
	sum_ = 0
	for digit in s[:-1]:
		if abs(ord(s[i]) - ord(s[i+1])) != 2:
			check = False
			break
		sum_ = sum_ + ord(s[i]) - ord('0')
		i += 1
	sum_ = sum_ + ord(s[-1]) - ord('0')
	if(check == True):
		if sum_ % 10 != 0:
			check = False
	if check == True:
		print("YES")
	else: 
		print("NO")