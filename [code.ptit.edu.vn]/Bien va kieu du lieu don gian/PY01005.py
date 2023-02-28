s = input()
count = 0
for digit in s:
	if digit == '4' or digit == '7':
		count += 1
if count == 4 or count == 7:
	print("YES")
else:
	print("NO")