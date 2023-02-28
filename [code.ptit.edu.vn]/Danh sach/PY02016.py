test = int(input())
for test_case in range(test):
	amount = int(input())
	numbers = list(map(int,input().split()))
	dic = {}
	for number in numbers:
		if number in dic:
			dic[number] = dic[number] + 1
		else:
			dic[number] = 1

	max_value = 0
	result = 0
	for key, value in dic.items():
		if value > max_value and value > amount / 2:
			max_value = value
			result = key
		elif value == max_value and value > amount / 2:
			if key < result:
				result = key
	if max_value > 0:
		print(result)
	else:
		print("NO")


