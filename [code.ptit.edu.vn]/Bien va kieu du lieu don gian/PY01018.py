while True:
	get = input().split()
	K = int(get[0])	
	if K == 0:
		break
	S = get[1]

	P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
	S2 = ""
	for char in S:
		index = (P.index(char) + K) % 28
		S2 = P[index] + S2
	print(S2)