n = input()
i = -1
result = ""
while i >= -(len(n)):
	result = n[i] + result
	if i % 3 == 0 and i != -(len(n)):
		result = "," + result
	i -= 1
print(result)
