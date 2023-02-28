import itertools

t = int(input())
for test in range(t):
	N = int(input())
	char = [str(x) for x in range(1, N + 1)]
	char = sorted(char, reverse = True)
	a = itertools.permutations(char)
	count = 0
	for mem in a:
		count += 1
	print(count)
	for mem in itertools.permutations(char):
		tmp = "".join(mem)
		print(tmp, end = ' ')
	print()