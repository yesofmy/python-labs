'''Продемонструвати роботу з використанням спеціальних полів та методів. Крім того, що виконати завдання по списку, то ще і для кожного завдання вивести спеціальні поля для класу 
 і для екземпляру, такі як у таблиці з лекції 5 (13), ст. 1-2. Продемонструвати детальну роботу з класом.
bases
dict
doc
module
mro
name
qualname
Створіть клас, який представляє 3D-вектор. Реалізуйте метод для перетворення об'єкта в ціле число (__int__), обчислення абсолютного значення вектора (__abs__) та отримання рядкового представлення вектора (__str__).
'''
import math


class Vector3D:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __int__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector3D(x={self.x}, y={self.y}, z={self.z})"


vector = Vector3D(3, 4, 12)

print(f"String representation: {vector}")
print(f"Integer representation: {int(vector)}")
print(f"Absolute value: {abs(vector)}")


print("\nClass metadata:")
print(f"__bases__: {Vector3D.__bases__}")
print(f"__dict__: {Vector3D.__dict__}")
print(f"__doc__: {Vector3D.__doc__}")
print(f"__module__: {Vector3D.__module__}")
print(f"__mro__: {Vector3D.__mro__}")
print(f"__name__: {Vector3D.__name__}")
print(f"__qualname__: {Vector3D.__qualname__}")

print("\nInstance metadata:")
print(f"Instance __dict__: {vector.__dict__}")
