res = {}

def fee(s1, s2):
	if s1 == "Xe_con" and s2 == "5":
		return 10000
	if s1 == "Xe_con" and s2 == "7":
		return 15000
	if s1 == "Xe_tai":
		return 20000
	if s1 == "Xe_khach" and s2 == "29":
		return 50000
	if s1 == "Xe_khach" and s2 == "45":
		return 70000
	return 0

t = int(input())
for test in range(t):
	data = input().split()
	if data[4] not in res.keys():
		res[data[4]] = 0
	if data[3] == "IN":
		res[data[4]] += fee(data[1], data[2])
for key, value in res.items():
	print(f"{key}: {value}")
