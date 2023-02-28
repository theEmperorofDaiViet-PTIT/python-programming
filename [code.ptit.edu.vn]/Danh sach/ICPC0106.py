char = []
for i in range(ord('0'), ord('9') + 1):
	char.append(chr(i))
for i in range(ord('A'), ord('F') + 1):
	char.append(chr(i))

def convert(n, k):
	res = ""
	while n != 0:
		res = char[n % k] + res
		n = int(n / k)
	# if res[0].isnumeric() == False:
	# 	res = "0" + res
	if res != "":
		return res
	else:
		return "0"

t = int(input())
for test in range(t):
	k = int(input())
	n = int(input(), 2)
	print(convert(n, k))