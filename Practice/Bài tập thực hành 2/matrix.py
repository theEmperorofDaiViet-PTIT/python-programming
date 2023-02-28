class Matrix():
    def  __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def addition(self):
        if (len(self.matrix1) != len(self.matrix2)) | (len(self.matrix1[0]) != len(self.matrix2[0])) :
            return None
        else:
            result = [[self.matrix1[i][j] + self.matrix2[i][j]  for j in range(len(self.matrix1[0]))] for i in range(len(self.matrix1))]
            return result

    def multi(self):
        if len(self.matrix1[0]) != len(self.matrix2):
            return None
        else:
            res = [[0 for x in range(len(self.matrix2[0]))] for y in range(len(self.matrix1))] 
            for i in range(len(self.matrix1)):
                for j in range(len(self.matrix2[0])):
                    for k in range(len(self.matrix2)):
                        res[i][j] += self.matrix1[i][k] * self.matrix2[k][j]
            return res

X = [[12,7,3],
    [4,5,6]]

Y = [[5,8,3],
    [6,7,3],
    [4,5,3]]

matrix = Matrix(X, Y)
print(matrix.addition())
print(matrix.multi())
        