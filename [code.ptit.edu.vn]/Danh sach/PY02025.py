l = list(map(int,input().split()))
n = l[0]
m = l[1]
a = list(map(int,input().split()))
A = set(a)
A = sorted(A)
b = list(map(int,input().split()))
B = set(b)
B = sorted(B)
A_B = []
B_A = []
for mem in A:
	if mem in B:
		print(mem, end = ' ')
		continue
	A_B.append(mem)
print()
for mem in B:
	if mem in A:
		continue
	B_A.append(mem)
for mem in A_B:
	print(mem, end = ' ')
print()
for mem in B_A:
	print(mem, end = ' ')
print()
