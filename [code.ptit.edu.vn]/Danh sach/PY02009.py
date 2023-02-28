test = int(input())
for t in range(test):
	N = int(input())
	stat = {}
	for n in range(N):
		i = int(input())
		if i in stat:
			stat[i] += 1
		else:
			stat[i] = 1
	min_value = -1
	max_appearence = 0
	for key,value in stat.items():
		if value > max_appearence:
			max_appearence = value
			min_value = key
		elif value == max_appearence:
			if key < min_value:
				min_value = key
	print(min_value)
