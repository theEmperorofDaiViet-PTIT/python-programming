def check(n):
	if n < 10:
		return False
	s = str(n)
	if s == s[::-1]:
		return True
	else:
		return False

N, M = [int(x) for x in input().split()]
matrix = []
for i in range(N):
	row = [int(x) for x in input().split()]
	matrix.append(row)

maximum = 0
for i in range(N):
	for j in range(M):
		if check(matrix[i][j]) == True and matrix[i][j] > maximum:
			maximum = matrix[i][j]
if maximum == 0:
	print("NOT FOUND")
else:
	print(maximum)
	for i in range(N):
		for j in range(M):
			if matrix[i][j] == maximum:
				print(f"Vi tri [{i}][{j}]")

