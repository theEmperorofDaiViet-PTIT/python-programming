import math

N = int(input())
Matrix = []
for i in range(N):
	row = list(input())
	Matrix.append(row)

res = 0
for i in range(N):
	count = 0
	for j in range(N):
		if Matrix[i][j] == "C":
			count += 1
	if count >= 2:
		res += math.factorial(count) / (2 * (math.factorial(count - 2)))

for i in range(N):
	count = 0
	for j in range(N):
		if Matrix[j][i] == "C":
			count += 1
	if count >= 2:
		res += math.factorial(count) / (2 * (math.factorial(count - 2)))
print(int(res))