def killZero(s):
	s2 = "";
	for i in range(0,len(s)):
		if s[i] != '0':
			for j in range(i,len(s)):
				s2 += s[j]
			break
	if s2 == "":
		return s
	return s2

def findMin(l, lenlist):
	mins = []
	minlen = min(lenlist)
	for s in l:
		if len(s) == minlen:
			mins.append(s)
	return min(mins)

def findMax(l, lenlist):
	maxs = []
	maxlen = max(lenlist)
	for s in l:
		if len(s) == maxlen:
			maxs.append(s)
	return max(maxs)

while True:
	t = int(input())
	if t == 0:
		break
	l = []
	lenlist = []
	for test in range(t):
		s = input()
		l.append(killZero(s))
		lenlist.append(len(killZero(s)))
	maximum = findMax(l,lenlist)
	minimum = findMin(l,lenlist)

	if maximum == minimum:
		print("BANG NHAU")
	else:
		print(f"{minimum} {maximum}")

# s = input()
# print(killZero(s))