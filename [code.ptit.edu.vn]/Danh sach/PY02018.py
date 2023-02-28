N = int(input())
a = list(map(int,input().split()))
for i in range(1,30000):
	if i not in a:
		print(i)
		break

