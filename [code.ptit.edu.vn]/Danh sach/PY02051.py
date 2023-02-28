def calculate(x,y,z):
	a = ((x+y+x) - 2*y) // 2
	b = ((x+y+x) - 2*z) // 2
	c = ((x+y+x) - 2*x) // 2
	return [a, b, c]

N = int(input())
l = []
for t in range(N):
	row = list(map(int,input().split()))
	l.append(row)
res = [0,] * N
for i in range(1,N-2):
	r = calculate(l[i][i+1],l[i+1][i+2],l[i][i+2])
	res[i-1] = r[0]
	res[i] = r[1]
	res[i+1] = r[2]
for mem in res:
	print(mem, end = ' ')
