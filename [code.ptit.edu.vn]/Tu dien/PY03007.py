#text = "ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!   vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11."
text = ""
while True:
	try:
		line = input()
		text += line + " "
	except EOFError:
		break

text1 = text.split('.')
text2 = []
text3 = []
for mem in text1:
	for member in mem.split('?'):
		text2.append(member)
for mem in text2:
	for member in mem.split('!'):
		text3.append(member)

res = []
for mem in text3:
	sen = ""
	for char in mem.split():
		if sen == "":
			if char != ' ':
				sen += char.title() + " "
		else:
			if char != ' ':
				sen += char.lower() + " "
	res.append(sen)

for mem in res:
	print(mem.strip())

# def Xuly (s):
#     res = []
#     ktdb = ['.', '?', '!']
#     s.lower()
#     tmp = ""
#     for i in range(0,len(s)):
#         if s[i] in ktdb:
#             res.append(tmp)
#             tmp = ""
#         else:
#             tmp += s[i]
            
#     for i in range(0, len(res)):
#         res[i] = " ".join(res[i].split())
#         res[i] = res[i].capitalize()
#         print(res[i])
   
# s = ""
# while 1:
#     try:
#         s += input()
#     except:
#         break
# Xuly(s)

# import re
# s=""
# while True:
#     try:
#         s=s+input()+" "
#     except EOFError:
#         break
# s=re.split("[\.\?\!]",s)
# for i in s:
#     if i!='':
#         i=i.strip().capitalize()
#         i=re.sub('\s+',' ',i)
#         print(i)