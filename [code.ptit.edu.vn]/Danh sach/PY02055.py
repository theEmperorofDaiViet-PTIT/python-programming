isPRIME = [True] * 1001
isPRIME[0] = isPRIME[1] = False

i = 2
while i * i <= 1000:
	if isPRIME[i] == True:
		for j in range(i * i, 1001, i):
			isPRIME[j] = False
	i += 1


N, M = [int(x) for x in input().split()]
matrix = []
for i in range(N):
	row = [int(x) for x in input().split()]
	matrix.append(row)

maximum = 0
for i in range(N):
	for j in range(M):
		if isPRIME[matrix[i][j]] == True and matrix[i][j] > maximum:
			maximum = matrix[i][j]
if maximum == 0:
	print("NOT FOUND")
else:
	print(maximum)
	for i in range(N):
		for j in range(M):
			if matrix[i][j] == maximum:
				print(f"Vi tri [{i}][{j}]")

