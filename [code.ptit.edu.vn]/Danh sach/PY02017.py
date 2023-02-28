t = int(input())
for test in range(t):
	N = int(input())
	l = list(map(int,input().split()))
	l = sorted(l)
	if len(l) == 1:
		print(l[0])
	else:
		for i in range(1,len(l)):
			if l[i] != l[i-1]:
				if i % 2 == 1:
					print(l[i-1])
					break
			if i == len(l) - 1:
				print(l[i])
				break