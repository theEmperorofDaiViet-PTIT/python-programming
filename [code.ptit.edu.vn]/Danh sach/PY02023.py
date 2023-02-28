def sum_digits(n):
	sum_ = 0
	while n != 0:
		sum_ = sum_ + (n % 10)
		n = n // 10
	return sum_
test = int(input())
for t in range(test):
	N = int(input())
	a = list(map(int,input().split()))
	for i in range(1,len(a)):
		temp = a[i]
		tmp = sum_digits(a[i])
		j = i - 1
		while j >= 0 and (tmp < sum_digits(a[j]) or (tmp == sum_digits(a[j]) and temp < a[j])):
			a[j+1] = a[j]
			j -= 1
		a[j+1] = temp
	for mem in a:
		print(f"{mem} ", end = '')
	print('')