'''Продемонструйте створення абстрактного класу (мінімум на 3 методи). А далі реалізуйте похідні 2 класи. Продемонструйте просту роботу з класами та реалізуйте виникнення помилок, 
про які говориться в лекції (а потім приберіть ті помилки). Класи - власна ваша розробка, які хочете, але щоб відповідали правилам створення абстрактних класів.'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        """площа"""
        pass

    @abstractmethod
    def perimeter(self):
        """периметр"""
        pass

    @abstractmethod
    def draw(self):
        """малювання"""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Обчислюємо площу кола."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Обчислюємо периметр кола."""
        return 2 * math.pi * self.radius

    def draw(self):
        """Просте представлення малювання кола."""
        return f"Drawing a circle with radius {self.radius}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Обчислюємо площу прямокутника."""
        return self.width * self.height

    def perimeter(self):
        """Обчислюємо периметр прямокутника."""
        return 2 * (self.width + self.height)

    def draw(self):
        """Просте представлення малювання прямокутника."""
        return f"Drawing a rectangle with width {self.width} and height {self.height}"



circle = Circle(5)
rectangle = Rectangle(4, 6)

print(circle.area())
print(circle.perimeter())
print(circle.draw())

print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.draw())

try:
    shape = Shape()
except TypeError as e:
    print(f"Error: {e}")