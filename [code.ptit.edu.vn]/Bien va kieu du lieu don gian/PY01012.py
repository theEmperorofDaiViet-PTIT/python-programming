s1 = input()
s2 = input()
index = int(input()) - 1
s = s1[:index] + s2 + s1[index:]
print(s)

