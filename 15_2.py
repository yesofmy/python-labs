class Matrix:
    
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матриці повинні мати однакові розміри для додавання.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] 
                  for i in range(len(self.matrix))]
        return Matrix(result)

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матриці повинні мати однакові розміри для віднімання.")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] 
                  for i in range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці.")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))) 
                   for j in range(len(other.matrix[0]))] 
                  for i in range(len(self.matrix))]
        return Matrix(result)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def __repr__(self):
        return f"Matrix({self.matrix})"


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

print("Matrix1:")
print(matrix1)

print("\nMatrix2:")
print(matrix2)

print("\nAddition (Matrix1 + Matrix2):")
print(matrix1 + matrix2)

print("\nSubtraction (Matrix1 - Matrix2):")
print(matrix1 - matrix2)


print("\nMultiplication (Matrix1 * Matrix2):")
print(matrix1 * matrix2)

print("\nClass metadata:")
print(f"__bases__: {Matrix.__bases__}")
print(f"__dict__: {Matrix.__dict__}")
print(f"__doc__: {Matrix.__doc__}")
print(f"__module__: {Matrix.__module__}")
print(f"__mro__: {Matrix.__mro__}")
print(f"__name__: {Matrix.__name__}")
print(f"__qualname__: {Matrix.__qualname__}")
print("\nInstance metadata:")
print(f"Instance __dict__: {matrix1.__dict__}")