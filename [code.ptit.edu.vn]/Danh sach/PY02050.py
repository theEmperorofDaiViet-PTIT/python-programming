def count(l, n):
	l.reverse()
	n = len(l) - 1 - n
	count = 1
	for i in range(n + 1, len(l)):
		if l[i] <= l[n]:
			count += 1
		else:
			break
	l.reverse()
	return count

t = int(input())
for test in range(t):
	length = int(input())
	li = list(map(int, input().split()))
	for i in range(len(li)):
		print(count(li, i), end = ' ')
	print()