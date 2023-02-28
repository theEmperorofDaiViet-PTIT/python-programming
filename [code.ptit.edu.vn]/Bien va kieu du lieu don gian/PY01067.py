import itertools

t = int(input())
for test in range(t):
	n = int(input())
	char = ['0', '1', '2']
	count = 0
	length = 1
	while count < n:
		for mem in itertools.product(char, repeat = length):
			if count == n:
				break
			tmp = "".join(mem)
			if tmp.count("2") > len(tmp) // 2 and tmp[0] != "0":
				count += 1
				print(tmp, end = ' ')
		length += 1
	print()
			
