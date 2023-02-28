### Bài tập 1

def check_number(num):
    s = 0
    for i in range(1, num):
        if num%i == 0:
            s += i
    if s > num:
        return True
    else:
        return False
    
number = int(input("Nhập số cần kiểm tra: "))
check_number(number)

### Bài tập 2

arr = []
for i in range(1, 1000):
    if check_number(i):
        arr.append(i)
print(f"Số phong phú thứ 50: {arr[49]}")

num = 1
count = 0
while count < 50:
    if check_number(num):
        count += 1
    num += 1
    
print(f"Số phong phú thứ 50: {num - 1}")

### Bài tập 3

def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True
print(isPalindrome('madam'))

def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
print(isPalindrome('mada'))

### Bài tập 4

strings = ''' The most familiar palindromes in English are character-unit palindromes. 
The characters read the same backward as forward. 
Some examples of palindromic words are redivider, deified, civic, radar, 
level, rotor, kayak, reviver, racecar, madam, and refer.'''

strings = strings.replace(".", "")
strings = strings.replace(",", "")
strings = strings.replace("\n", "")
words = strings.split()
words = [w.strip() for w in words]
words = list(set(words))
lst_Palindrome = []
for word in words:
    if isPalindrome(word):
        lst_Palindrome.append(word)
        
max(lst_Palindrome, key=len)

### Bài tập 5

def sum_multiple(*arg):
    s = 0
    mul = 1
    for num in arg:
        s += num
        mul *= num
    return s, mul

Sum, Mul = sum_multiple(1, 5, 5, 8, 7, 9, 8)
print(f"Tổng: {Sum}, Tích: {Mul}")

### Bài tập 6

def concatnate(**kwargs):
    string = ""
    for k, v in kwargs.items():
        string += v + " "
    return string.strip()
        
concatnate(arg1 = 'Welcome', arg2 = 'To', arg3 = 'Python', arg4 = '!!!!!')

### Bài tập 7

def solution(a, b):
    if a == 0:
        if b!=0:
            print("Phương trình vô nghiệm")
        else:
            print("Phương trình vô số nghiệm")
    else:
        return -b/a
    
x = solution(2, 6)
print(x)

### Bài tập 8

import math

def solution_quadratic(a, b, c):
    if a == 0:
        return solution(b, c)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            return -b/2*a
        else:
            return ((-b + math.sqrt(delta)/2*a, (-b - math.sqrt(delta)/2*a)))

x = solution_quadratic(2, 9, 7)
print(x)
                                       