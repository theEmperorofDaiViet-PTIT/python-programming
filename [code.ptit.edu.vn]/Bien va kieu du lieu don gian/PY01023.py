import math
test = int(input())
for test_case in range(test):
	n = int(input())
	dic = {}
	while n % 2 == 0:
		if 2 in dic:
			dic[2] += 1
		else:
			dic[2] = 1
		n = n / 2
	for i in range(3,int(math.sqrt(n)+1),2):
		while n % i == 0:
			if i in dic:
				dic[i] += 1
			else:
				dic[i] = 1
			n = n / i
	if n > 2:
		dic[n] = 1
	print(f"{1} ", end = '')
	for key, value in dic.items():
		print(f"* {int(key)}^{int(value)} ", end = '')
	print('')