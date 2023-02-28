import math
N = int(input())
m = []
for i in range(N):
	line = input()
	row = []
	for mem in line:
		row.append(mem)
	m.append(row)
count = 0
for i in range(N):
	tmp = 0
	for j in range(N):
		if m[i][j] == 'C':
			tmp += 1
	if tmp > 1:
		count += int(math.factorial(tmp) / (math.factorial(2) * math.factorial(tmp - 2)))
for j in range(N):
	tmp = 0
	for i in range(N):
		if m[i][j] == 'C':
			 tmp += 1
	if tmp > 1:
		count += int(math.factorial(tmp) / (math.factorial(2) * math.factorial(tmp - 2)))
print(count)