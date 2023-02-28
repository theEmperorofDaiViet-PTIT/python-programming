N = int(input())
l = [int(x) for x in input().split()]

positive = []
negative = []
for mem in l:
	if mem > 0:
		positive.append(mem)
	elif mem < 0:
		negative.append(mem)

positive = sorted(positive)
negative = sorted(negative)
res = []
# 3 pos
if len(positive) >= 3:
	res.append(positive[-1] * positive[-2] * positive[-3])

# 2 pos
if len(positive) == 2:
	res.append(positive[-1] * positive[-2])

# 1 pos 2 neg
if len(positive) >= 1 and len(negative) >= 2:
	res.append(positive[-1] * negative[0] * negative[1])

# 2 neg
if len(negative) >= 2:
	res.append(negative[0] * negative[1])

# 0
if 0 in l:
	res.append(0)

# 2 pos 1 neg
if len(positive) >= 2 and len(negative) >= 1:
	res.append(positive[0] * positive[1]* negative[-1])

# 3 neg
if len(negative) >= 3:
	res.append(negative[-3] * negative[-2] * negative[-1])

print(max(res))