s = input()
res = ""
for char in s:
	if char.islower() == True:
		res += char.upper()
	else:
		res += char.lower()
print(res)