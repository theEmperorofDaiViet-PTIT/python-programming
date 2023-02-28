import itertools
char = ['2', '3', '5', '7']
n = int(input())
for i in range(4, n+1):
	for mem in itertools.product(char, repeat = i):
		check = True
		tmp = "".join(mem)
		for m in char:
			if tmp.find(m) == -1:
				check = False
				break
		if tmp[-1] == '2':
			check = False
		if check == True:
			print(tmp)