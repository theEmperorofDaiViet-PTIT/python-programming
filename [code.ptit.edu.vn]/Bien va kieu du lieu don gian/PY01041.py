def checkDiff(s,n):
	s1 = s[0:n+1]
	set1 = set(s1)
	s2 = s[n:len(s)]
	set2 = set(s2)
	if len(s1) == len(set1) and len(s2) == len(set2):
		return True
	else:
		return False

def checkIncDec(s,n):
	s1 = s[0:n+1]
	ss1 = "".join(sorted(s1))
	s2 = s[n:len(s)]
	ss2 = "".join(sorted(s2, reverse = True))
	if s1 == ss1 and s2 == ss2:
		return True
	else:
		return False

t = int(input())
for test in range(t):
	s = input()
	found = False
	for i in range(1,len(s)-1):
		if checkDiff(s,i) == True and checkIncDec(s,i) == True:
			found = True
			break
	if found == True:
		print("YES")
	else:
		print("NO")
		
