test = int(input())
for test_case in range(test):
	s = input()
	sum_ = 0
	for digit in s:
		sum_ = sum_ + ord(digit) - ord('0')
	if sum_ % 3 == 0:
		print("YES")
	else:
		print("NO")