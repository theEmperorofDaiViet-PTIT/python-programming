numbers = list(map(int, input().split()))
while numbers != [0, 0, 0, 0]:
	count = 0
	while not(numbers[0] == numbers[1] == numbers[2] == numbers[3]):
		temp = numbers[0]
		i = 0
		for number in numbers[:-1]:
			numbers[i] = abs(numbers[i] - numbers[i+1])
			i += 1
		numbers[i] = abs(numbers[i] - temp)
		count += 1
	print(count)
	numbers = []
	numbers = list(map(int, input().split()))