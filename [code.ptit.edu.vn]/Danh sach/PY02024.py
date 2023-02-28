def mul_digits(n):
	mul_ = 1
	while n != 0:
		mul_ = mul_ * (n % 10)
		n = n // 10
	return mul_
test = int(input())
for t in range(test):
	N = int(input())
	a = list(map(int,input().split()))
	for i in range(1,len(a)):
		temp = a[i]
		tmp = mul_digits(a[i])
		j = i - 1
		while j >= 0 and (tmp < mul_digits(a[j]) or (tmp == mul_digits(a[j]) and temp < a[j])):
			a[j+1] = a[j]
			j -= 1
		a[j+1] = temp
	for mem in a:
		print(f"{mem} ", end = '')
	print('')