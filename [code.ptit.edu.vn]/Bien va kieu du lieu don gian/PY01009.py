test = input()
hoa = 0
thuong = 0
for character in test:
	if character >= 'A' and character <= 'Z':
		hoa += 1
	elif character >= 'a' and character <= 'z':
		thuong += 1
if hoa > thuong:
	test = test.upper()
elif hoa <= thuong:
	test = test.lower()
print(test)