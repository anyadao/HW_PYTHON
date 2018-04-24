# 34. Создать два класса: Окружность и Точка.
# Создать в классе окружности метод, который принимает в качестве параметра точку и проверяет находится ли
# данная точка внутри окружности.

import math

class Circle:

    def __init__(self, center_x=0, center_y=0,  radius=0):
        self.center_x = center_x
        self.center_y = center_y
        self._radius = radius

    def is_in_circle(self, Point):
        self.difference = math.sqrt((Point.coord_x - self.center_x)**2 + (Point.coord_y - self.center_y)**2)
        if self.difference < self._radius:
            print('Точка находится в окружности. ')
            return True
        elif self.difference == self._radius:
            print('Точка находится на окружности. ')
            return True
        else:
            print('Точка не находится в окружности. ')
            return False

    def print_info(self, Point):
        print('Координаты окружности: %d см., %d см.; радиус: %d см.' %(self.center_x, self.center_y, self._radius))
        print('Координаты точки: %d см., %d см.' %(Point.coord_x, Point.coord_y))
        print('____________________________________________________________________________________________________')

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Negative value')
        else:
            self._radius = radius
class Point:

    def __init__(self, coord_x=0, coord_y=0):
        self.coord_x = coord_x
        self.coord_y = coord_y

circle1 = Circle(10, 11)
circle1.radius = 5
point1 = Point(10, 11)
circle1.is_in_circle(point1)
circle1.print_info(point1)

circle2 = Circle(5, 13)
circle2.radius = 8
point2 = Point(23, 26)
circle2.is_in_circle(point2)
circle2.print_info(point2)