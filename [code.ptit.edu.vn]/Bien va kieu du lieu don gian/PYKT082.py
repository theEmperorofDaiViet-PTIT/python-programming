import math
def convert(n):
	if n >= 39:
		return 9.0
	elif n >= 37:
		return 8.5
	elif n >= 35:
		return 8.0
	elif n >= 33:
		return 7.5
	elif n >= 30:
		return 7.0
	elif n >= 27:
		return 6.5
	elif n >= 23:
		return 6.0
	elif n >= 20:
		return 5.5
	elif n >= 16:
		return 5.0
	elif n >= 13:
		return 4.5
	elif n >= 10:
		return 4.0
	elif n >= 7:
		return 3.5
	elif n >= 5:
		return 3.0
	elif n >= 3:
		return 2.5
	else:
		return 0

def calculate(r, l, s, w):
	score = (r + l + s + w) / 4
	tmp = float("0." + str(score).split('.')[1])

	if tmp >= 0.75:
		score = math.ceil(score)
	elif tmp >= 0.25: 
		score = math.floor(score) + 0.5
	else:
		score = math.floor(score)
	return float(score)

t = int(input())
for test in range(t):
	data = list(map(float, input().split()))
	r = convert(data[0])
	l = convert(data[1])
	s = data[2]
	w = data[3]
	print(calculate(r, l, s, w))