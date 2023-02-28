t = int(input())
for test in range(t):
	noti = input()
	wordset = noti.split()
	res = ""
	for mem in wordset:
		if len(res + mem) < 100:
			res += mem + " "
		else:
			break
	print(res)
