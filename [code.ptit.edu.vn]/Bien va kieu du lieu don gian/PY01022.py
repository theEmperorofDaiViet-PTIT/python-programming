n = input()
step = 0
while len(n) >= 2:
	sum_ = 0
	for char in n:
		sum_ += ord(char) - ord('0')
	n = str(sum_)
	step += 1
print(step)