test = int(input())
for t in range(test):
	n = input()
	mul = 1
	for char in n:
		if char != '0':
			mul = mul * int(char)
	print(mul)
