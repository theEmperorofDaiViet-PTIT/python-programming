from collections import defaultdict
n = int(input())
text = ""
for i in range(n):
	text += input() + " "
totalLength = len(text.split())
wordset = set(text.split())
wordset = sorted(wordset)
res = defaultdict(int)
for mem in wordset:
	c = text.count(mem)
	TF = c / totalLength
	res[mem] = TF

for k in sorted(res, key = res.get, reverse = True):
	print(k, end = ' ')
	print("%.2f" % res.get(k))