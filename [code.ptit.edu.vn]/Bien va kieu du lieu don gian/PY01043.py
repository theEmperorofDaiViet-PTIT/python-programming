import itertools
t = int(input())
for test in range(t):
	n = input()
	length = len(n) // 2
	for i in range(1, length + 1):
		for roll in itertools.product(['0', '2', '4', '6', '8'], repeat = i):
			if roll[0] == '0':
				continue
			s = "".join(roll) + "".join(roll)[::-1]
			if int(s) < int(n):
				print(s, end = ' ')
	print()
