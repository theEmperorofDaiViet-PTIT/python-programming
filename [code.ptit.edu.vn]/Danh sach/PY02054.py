def solve1(matrix, N, M):
	d = N - M
	ignore = []
	ig = 0
	for i in range(d):
		ignore.append(ig)
		ig += 2

	for i in range(N):
		if i in ignore:
			continue
		else:
			for mem in matrix[i]:
				print(mem, end = ' ')
			print()
	return

def solve2(matrix, N, M):
	d = M - N
	ignore = []
	ig = 1
	for i in range(d):
		ignore.append(ig)
		ig += 2

	for i in range(N):
		for j in range(M):
			if j in ignore:
				continue
			else:
				print(matrix[i][j], end = ' ')
		print()



N, M = [int(x) for x in input().split()]
matrix = []
for i in range(N):
	row = [int(x) for x in input().split()]
	matrix.append(row)
if N >= M:
	solve1(matrix, N, M)
else:
	solve2(matrix, N, M)



