amount = 0
numbers = []
while amount < 10:
	get_input = list(map(int, input().split()))
	for got_input in get_input:
		numbers.append(got_input)
		amount = len(numbers)
		if amount == 10:
			break
set_numbers = set()
for number in numbers:
	set_numbers.add(number % 42)
print(len(set_numbers))