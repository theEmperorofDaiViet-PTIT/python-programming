test = int(input())
def check_locphat():
	Test = input()
	if len(Test) >= 2 and Test[-1] == '6' and Test[-2] == '8':
		return "YES"
	else:
		return "NO"

for number_test in range(test):
	print(check_locphat())
