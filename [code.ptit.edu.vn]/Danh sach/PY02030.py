isPRIME = [True] * 1000008
isPRIME[0] = isPRIME[1] = False

i = 2
while i * i <= 1000007:
	if isPRIME[i] == True:
		for j in range(i * i, 1000008, i):
			isPRIME[j] = False
	i += 1

def check(s, k):
	sum1, sum2 = 0, 0
	for i in range(0, k + 1):
		sum1 += s[i]
	for i in range(k + 1, len(s)):
		sum2 += s[i]
	if isPRIME[sum1] == True and isPRIME[sum2] == True:
		return True
	else:
		return False

n = int(input())
l = [int(x) for x in input().split()]
s = []
for mem in l:
	if mem not in s:
		s.append(mem)

found = False
for i in range(0, len(s)):
	if check(s, i) == True:
		found = True
		print(i)
		break
if found == False:
	print("NOT FOUND")
