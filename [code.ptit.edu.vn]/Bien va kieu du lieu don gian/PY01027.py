s = input()
check = True
for char in s:
	if char != '6' and char != '8':
		check = False
		break
if check == True:
	if s.find('8') == 0:
		check = False
	if s.find('888') != -1:
		check = False
if check == True:
	print('YES')
else:
	print('NO')