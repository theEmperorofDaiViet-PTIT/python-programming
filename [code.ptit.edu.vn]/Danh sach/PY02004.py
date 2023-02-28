amount = int(input())
numbers = list(map(int,input().split()))
count = 0
i = 1
for number in numbers[1:]:
	if numbers[i-1] != numbers[i]:
		count += 1
	i += 1
print(count)