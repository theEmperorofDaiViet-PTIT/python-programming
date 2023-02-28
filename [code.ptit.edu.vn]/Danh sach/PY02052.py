N = int(input())
matrix = []
for i in range(N):
	row = [int(x) for x in input().split()]
	matrix.append(row)
K = int(input())

up = 0
down = 0
for i in range(N):
	for j in range(N):
		if i < j:
			up += matrix[i][j]
		if i > j:
			down += matrix[i][j]

d = abs(up - down)
if d <= K:
	print("YES")
else:
	print("NO")
print(d)