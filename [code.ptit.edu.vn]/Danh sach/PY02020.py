t = int(input())
l0 = list(map(float,input().split()))
min_ = min(l0)
max_ = max(l0)
while min_ in l0:
	l0.remove(min_)
while max_ in l0:
	l0.remove(max_)
# print(l0)
# l1 = [value for value in l0 if value != min(l0)]
# l = [value for value in l1 if value != max(l1)]
if len(l0) != 0:
	sum_ = 0
	for i in l0:
		sum_ += i
	avg = sum_ / len(l0)
	print("%.2f"% avg)