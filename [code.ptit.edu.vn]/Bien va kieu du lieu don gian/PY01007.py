test = int(input())
for test_case in range(test):
	numbers = list(map(float,input().split()))
	count = 0
	numbers[1] /= 100

	while numbers[0] < numbers[2]:
		numbers[0] = numbers[0] + numbers[0] * numbers[1]
		count += 1
	print(count)