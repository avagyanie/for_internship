"""
Пожалуйста, не пишите код внутри формы ответов, разместите его на Github и приложите ссылку. Если в задании что-то непонятно, опишите возникшие вопросы и сделанные предположения. Например, в комментариях в коде.

Задание:

Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:

Юнит-тесты
Легкость добавления других фигур
Вычисление площади фигуры без знания типа фигуры в compile-time
Проверку на то, является ли треугольник прямоугольным
"""


class Shape:
    def calculate_area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")
        self.radius = radius

    def calculate_area(self):
        pi = 3.141592653589793
        return pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be greater than zero.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The given sides don't form a triangle.")
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10

def calculate_shape_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("shape must be an instance of Shape")
    return shape.calculate_area()


def main():
  
    circle_radius = 5
    circle = Circle(circle_radius)
    print(f"Circle with radius {circle_radius}:")
    print(f"Area: {circle.calculate_area()}")
    
    triangle_sides = (3, 4, 5)
    triangle = Triangle(*triangle_sides)
    print(f"\nTriangle with sides {triangle_sides}:")
    print(f"Area: {triangle.calculate_area()}")
    print(f"Is Right-Angled: {triangle.is_right_angle()}")
    
    print(f"\nUsing calculate_shape_area function:")
    print(f"Circle Area: {calculate_shape_area(circle)}")
    print(f"Triangle Area: {calculate_shape_area(triangle)}")

if __name__ == "__main__":
    print(main())
