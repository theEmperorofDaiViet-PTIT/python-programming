# N = int(input())
# res = {}
# separator = [' ', ',', '.', '?', '!', ':', ';', '/', '-', '(', ')']
# for t in range(N):
# 	line = input().lower()
# 	line.strip()
# 	word = ""
# 	for mem in line:
# 		if mem in separator:
# 			if word != "":
# 				if word in res:
# 					res[word] += 1
# 				else:
# 					res[word] = 1
# 			word = ""
# 		else:
# 			word += mem
# l = sorted(res.items(), key = lambda k: (-k[1], k[0]))
# for mem in l:
# 	print(f"{mem[0]} {mem[1]}")

def run():
    n = int(input())
    a = []
    # nhap van ban
    for i in range(n):
        x = input().lower()
        x = x.replace(".","")
        x = x.replace(",","")
        x = x.replace("!","")
        x = x.replace(":","")
        x = x.replace(";","")
        x = x.replace("-"," ")
        x = x.replace("/"," ")
        x = x.split()
        a.append(x)
    # a.sort()
    dict = {}
    for i in a:
        # i = i.split()
        for j in i:
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
    sorted_dict = sorted(dict.items(), key = lambda x: (-x[1], x[0]))
    for i in sorted_dict:
        print(i[0],i[1])
run()