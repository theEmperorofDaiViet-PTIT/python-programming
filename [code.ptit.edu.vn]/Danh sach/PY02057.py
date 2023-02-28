N, M = [int(x) for x in input().split()]
matrix = []
for i in range(N):
	row = [int(x) for x in input().split()]
	matrix.append(row)

maximum = 0
for i in range(N):
	for j in range(M):
		if matrix[i][j] > maximum:
			maximum = matrix[i][j]

minimum = maximum
for i in range(N):
	for j in range(M):
		if matrix[i][j] < minimum:
			minimum = matrix[i][j]


d = maximum - minimum
found = False
for i in range(N):
	for j in range(M):
		if matrix[i][j] == d:
			found = True
			break
	if found == True:
		break

if found == False:
	print("NOT FOUND")
else:
	print(d)
	for i in range(N):
		for j in range(M):
			if matrix[i][j] == d:
				print(f"Vi tri [{i}][{j}]")
