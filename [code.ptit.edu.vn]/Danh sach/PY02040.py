N = int(input())
Matrix = []
for i in range(N):
	row = list(map(int, input().split()))
	Matrix.append(row)
K = int(input())
up = 0
down = 0
for i in range(N):
	for j in range(N):
		if i < N - 1 - j:
			up += Matrix[i][j]
		elif i > N - 1 - j:
			down += Matrix[i][j]
if abs(up - down) <= K:
	print("YES")
else:
	print("NO")
print(abs(up - down))