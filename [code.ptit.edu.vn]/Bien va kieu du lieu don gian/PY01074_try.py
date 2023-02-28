def summ(n):
	res = 0
	i = 2
	while n > 1:
		if n % i == 0:
			n = int(n / i)
			res += i
		else:
			i += 1
	if res == 0:
		res = n
	return res

t = int(input())
result = 0
for test in range(t):
	n = int(input())
	result += summ(n)
print(res)
