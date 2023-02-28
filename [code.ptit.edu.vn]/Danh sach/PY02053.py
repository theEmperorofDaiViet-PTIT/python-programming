N = int(input())
matrix = []
for i in range(N):
	row = list(map(int,input().split()))
	matrix.append(row)
K = int(input())

sum_above = 0
sum_below = 0
for i in range(N):
	for j in range(N):
		if i < N - j - 1:
			sum_above += matrix[i][j]
		elif i > N - j - 1:
			sum_below += matrix[i][j]
d = abs(sum_above - sum_below)
if d <= K:
	print("YES")
else:
	print("NO")
print(d)