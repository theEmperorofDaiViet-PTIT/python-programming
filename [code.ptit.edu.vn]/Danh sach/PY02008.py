import math
def generate_PRIME(amount, list_):
	index = 1
	count = 0
	n = 3
	while count < amount:
		check = True
		for i in range(3, int(math.sqrt(n)) + 1, 2):
			if n % i == 0:
				check = False
				break
		if check == True:
			count += 1
			list_.append(list_[index] + n)
			index += 1
		n += 2


get = input().split()
amount = int(get[0]) - 1
list_ = []
list_.append(int(get[1]))
list_.append(list_[0] + 2)
generate_PRIME(amount, list_)
for mem in list_:
	print(f"{mem} ", end = '')
