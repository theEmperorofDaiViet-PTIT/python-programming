import itertools
import math
amount = int(input())
l = sorted(list(map(int, input().split())))
for mem in itertools.combinations(l, 2):
	if math.gcd(mem[0], mem[1]) == 1:
		print(f"{mem[0]} {mem[1]}")