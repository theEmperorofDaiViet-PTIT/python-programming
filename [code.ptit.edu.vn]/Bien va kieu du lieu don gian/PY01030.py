def GCD(a,b):
	while b != 0:
		tmp = b
		b = a % b
		a = tmp
	return a

def PRIMEtogether(a,b):
	if GCD(a,b) == 1:
		return True
	else:
		return False

l = list(map(int,input().split()))
a = l[0]
e = l[1]
s = 10 ** (e-1)
e = 10 ** e
count = 0
for i in range(s,e):
	if PRIMEtogether(a,i) == True:
		print(f"{i} ", end = '')
		count += 1
		if count == 10:
			count = 0
			print()
