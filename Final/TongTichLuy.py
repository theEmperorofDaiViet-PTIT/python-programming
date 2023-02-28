N = int(input())
data = [int(x) for x in input().split()]
l = []
for i in range(N):
	tmp = 0
	for j in range(i+1):
		tmp += data[j]
	l.append(tmp)
summ = 0
mul = 1
for mem in l:
	summ += mem
	mul *= mem
if len(l) == 0:
	mul = 0
print(f"{summ} {mul}")