N = int(input())
l = list(map(int, input().split()))
count = 0
res = []
for i in range(0, N-1):
	if l[i] * l[i+1] > 0:
		count += 1
		res.append(f"{l[i]} {l[i+1]}")

print(count, end = ' ')
if len(res) > 0:
	print(res[len(res) - 1])