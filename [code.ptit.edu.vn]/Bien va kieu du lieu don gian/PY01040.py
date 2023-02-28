Dict = {}
value = 0
for i in range(65,91):
	Dict[chr(i)] = value
	value += 1
def keyOf(val, Dict):
    for key, value in Dict.items():
         if val == value:
             return key 
    return "404 Not Found!"
t = int(input())
for test in range(t):
	s = input()
	l = int(len(s) / 2)
	s1 = s[0:l]
	s2 = s[l:len(s)]
	rotate1 = 0
	for mem in s1:
		rotate1 += Dict[mem]
	rotate2 = 0
	for mem in s2:
		rotate2 += Dict[mem]
	s11 = ""
	for mem in s1:
		s11 += keyOf((Dict[mem] + rotate1) % 26, Dict)
	s21 = ""
	for mem in s2:
		s21 += keyOf((Dict[mem] + rotate2) % 26, Dict)
	s12 = ""
	for i in range(0,len(s11)):
		s12 += keyOf(((Dict[s11[i]]) + Dict[s21[i]]) % 26, Dict)
	print(s12)