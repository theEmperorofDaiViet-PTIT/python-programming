def PRIME(a):
	if a < 2:
		return False
	if a % 2 == 0:
		if a == 2:
			return True
		else:
			return False
	for i in range(3,a,2):
		if a % i == 0:
			return False
	return True

rows_and_cols = list(map(int,input().split()))
rows = rows_and_cols[0]
cols = rows_and_cols[1]
matrix = []

for i in range(rows):
	tmp = list(map(int,input().split()))
	row = []
	for no in tmp:
		row.append(no)
	matrix.append(row)

for i in range(0,rows):
	for j in range(0,cols):
		if PRIME(matrix[i][j]) == True:
			matrix[i][j] = 1
		else:
			matrix[i][j] = 0

for i in range(0,rows):
	for j in range(0,cols):
		print(f"{matrix[i][j]} ", end = '')
		if j == cols - 1:
			print('')