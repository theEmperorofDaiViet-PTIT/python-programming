test = int(input())
for test_case in range(test):
	s = input()
	dic = {}
	index = 0
	for char in s:
		if char.isnumeric() == False:
			dic[char] = int(s[index+1])
			index += 2
	for key, value in dic.items():
		for loops in range(value):
			print(key, end = '')
	print("")

