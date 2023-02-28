amount = int(input())
l = list(map(int,input().split()))
dem = 0
for i in range(0,amount):
	for j in range(i+1,amount):
		if(l[i] > l[j]):
			dem += 1
print(dem)