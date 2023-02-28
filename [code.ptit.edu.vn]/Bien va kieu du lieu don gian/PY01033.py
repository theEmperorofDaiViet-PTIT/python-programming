def GCD(a,b):
	while b != 0:
		tmp = b
		b = a % b
		a = tmp
	return a

def PRIMEtogether(a,b,c):
	if GCD(a,b) == 1 and GCD(b,c) == 1 and GCD(a,c) == 1:
		return True
	else:
		return False

l = list(map(int,input().split()))
s = l[0]
e = l[1]
for i in range(s,e-1):
	for j in range(i+1,e):
		for k in range(j+1,e+1):
			if PRIMEtogether(i,j,k) == True:
				print(f"({i}, {j}, {k})")