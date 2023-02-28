t = int(input())
for test in range(t):
	s = input()
	check = True
	l = s.split(".")

	if len(l) != 4:
		check = False

	for mem in l:
		if mem.isnumeric() == False:
			check = False

	if check == True:
		for mem in l:
			if int(mem) > 255:
				check = False
				break

	if check == True:
		print("YES")
	else:
		print("NO")