import math
def PRIME(a):
	if a < 2:
		return False
	if a % 2 == 0:
		if a == 2:
			return True
		else:
			return False
	for i in range(3,a,2):
		if a % i == 0:
			return False
	return True

amount = int(input())
numbers = list(map(int,input().split()))
dic = {}
for number in numbers:
	if PRIME(number) == True:
		if number in dic:
			dic[number] += 1
		else:
			dic[number] = 1
for key, value in dic.items():
	print(f"{key} {value}") 