#### Bài tập 1
string = 'python is a powerful programming language.'
list_strings = string.split(" ")
list_strings.sort(reverse=True)
print(list_strings)

#### Bài tập 2
string = 'restartrestart'
char = string[0]
for i in string[1:]:
    string = string.replace(char, '$')
    string = char + string[1:]
print(string)

#### Bài tập 3

string = 'python programming'
even_index = ''
for i in range(len(string)):
    if i%2 == 0:
        even_index += string[i]   
print(even_index)

#### Bài tập 4
List = ['abcda', 'xyz', 'ssss', 1236, 1221]
count = 0
for i in List:
    if len(str(i))>2 and (str(i)[0] == str(i)[-1]):
            count += 1
print(count)

#### Bài tập 5

List = ['a', 'b']
n = 4
result = []
for i in range(1, n+1):
    for item in List:
        result.append(item+str(i))
print(result)

#### Bài tập 6
List = [38, 12, 55] 
List.sort(reverse=True)
num = ''
for i in List:
    num += str(i)
num = int(num)    
print(num)

#### Bài tập 7

List = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

Sum = [sum(i) for i in List]

index_max = Sum.index(max(Sum))

List[index_max]

num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

print(max(num, key=sum))

#### Bài tập 8

matrix=[
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]
Sum = 0
Multi = 1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j:
            Sum += matrix[i][j]
            Multi *= matrix[i][j]
            
print(f"Sum : {Sum}")
print(f"Multiple : {Multi}")

#### Bài tập 9
str1 = 'programming'
my_dict = {}
for letter in set(str1):
    my_dict[letter] = str1.count(letter)
print(my_dict)

#### Bài tập 10
#Cách 1 
list_keys = ["a", "b", "c", "d"]
list_values = [1, 2, 3, 4]
res = {}
for i in range(len(list_keys)):
    res[list_keys[i]] = list_values[i]
print(res)

#Cách 2 
list_keys = ["a", "b", "c", "d"]
list_values = [1, 2, 3, 4]
res = dict(zip(list_keys, list_values))
print(res)

#### Bài tập 11
strings = '''Python Open source software is made better when users can easily contribute code and documentation to fix bugs and add features. 
Python code strongly encourages community involvement in improving the software. 
Learn more about how to make Python better for everyone code code.'''

strings = strings.replace(".", "")
list_words = strings.split()
result = {}
for word in set(list_words):
    count = list_words.count(word)
    if count >= 3:
        result[word] = count
        
result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
print(result)

#### Bài tập 12
Dict = {'a':1, 'b':3, 'c':4, 'd':6}
list_values = list(Dict.values())
print(list_values)
print(f"Max value: {max(list_values)}")
print(f"Min value: {min(list_values)}")