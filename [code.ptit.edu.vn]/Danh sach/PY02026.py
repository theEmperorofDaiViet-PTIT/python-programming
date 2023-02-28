t = list(map(int,input().split()))
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
s1 = set(l1)
s2 = set(l2)
if s1 == s2:
	print('YES')
else:
	print('NO')