def gcd(a,b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a

def PRIME_together(a, b):
	if gcd(a,b) == 1:
		return True
	return False

amount = int(input())

numbers = list(map(int, input().split()))
numbers = sorted(numbers)
i = 1
for number in numbers:
	for num in numbers[i:]:
		if PRIME_together(number, num) == True:
			print(f"{number} {num}")
	i += 1