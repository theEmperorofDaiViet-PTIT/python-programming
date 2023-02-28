t = int(input())
for test in range(t):
	s = input()
	res = ""
	sum_ = 0
	for char in s:
		if char.isnumeric() == True:
			sum_ += int(char)
		else:
			res += char
	res = sorted(res)
	res += str(sum_)
	for char in res:
		print(char, end = '')
	print()