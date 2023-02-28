t = int(input())
tmp = 1
for test in range(t):
	s1 = input()
	s2 = input()
	print(f"Test {tmp}: ", end = '')
	if sorted(s1) == sorted(s2):
		print("YES")
	else:
		print("NO")
	tmp += 1
