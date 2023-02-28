def check(a,b):
	if abs(a - b) == 1:
		return True
	else:
		return False

n = int(input())
for test in range(n):
	amount = int(input())
	card = list(map(int, input().split()))
	fee = list(map(int, input().split()))
	found = False
	price = 100001
	for i in range(len(card)):
		if abs(card[i]) == 1 and fee[i] < price:
			price = fee[i]
			found = True
	for i in range(len(card)):
		for j in range(i+1, len(card)):
			if check(card[i],card[j]) == True and fee[i] + fee[j] < price:
				price = fee[i] + fee[j]
				found = True
	if found == True:
		print(price)
	else:
		print(-1)