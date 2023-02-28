test = int(input())
for test_case in range(test):
	amount = int(input())
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	A = sorted(A)
	B = sorted(B)
	dic = {}
	index = 0
	for num in A:
		dic[num] = B[index]
		index += 1
	check = True
	for key, value in dic.items():
		if key > value:
			check = False
			break
	if check == True:
		print("YES")
	else:
		print("NO")