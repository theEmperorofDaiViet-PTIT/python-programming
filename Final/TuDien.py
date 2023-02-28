K = int(input())
if K > 10 or K < 0:
	print("INVALID INPUT")
else:
	D = {}
	for k in range(K):
		a, b = input().split()
		D[a] = b
	summ = 0
	mul = 1
	empty = True
	for value in D.values():
		try:
			tmp = int(value)
		except ValueError:
			continue
		else:
			summ += tmp
			mul *= tmp
			empty = False

	if empty == True:
		mul = 0
		
	print(f"{summ} {mul}")
