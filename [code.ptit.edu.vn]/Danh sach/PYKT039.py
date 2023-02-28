t = int(input())
for test in range(t):
	N = int(input())
	A = sorted(list(map(int, input().split())))
	B = sorted(list(map(int, input().split())))
	check = True
	for i in range(N):
		if A[i] > B[i]:
			check = False
			break
	if check == True:
		print("YES")
	else:
		print("NO")