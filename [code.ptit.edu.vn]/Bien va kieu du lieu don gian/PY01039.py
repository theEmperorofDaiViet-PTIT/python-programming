t = int(input())
for test in range(t):
	s = input()
	diff0 = set()
	diff1 = set()
	diff2 = set()
	for mem in s:
		diff0.add(mem)
	for i in range(0,len(s),2):
		diff1.add(s[i])
	for i in range(1,len(s),2):
		diff2.add(s[i])
	if len(diff0) == 2 and len(diff1) == 1 and len(diff2) == 1:
		print("YES")
	else:
		print("NO")