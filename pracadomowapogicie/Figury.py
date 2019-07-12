#!/usr/bin/env python3
"""
It's very basic example. Assuming that we cannot use some advanced concepts
implementation is pretty straightforward and not 100% correct. It just shows
some OOP concepts.

Probably inheritance Rectangle -> Square breaks LISKOV subst. rule but we don't
implement a case when it's broken
"""
import math

from tkinter import BOTH, Canvas, mainloop, Tk


class Figure:
    display_margin_left = 10
    display_margin_top = 10

    def __init__(self, color):
        self.color = color
        self.canvas = Canvas(Tk(), width=600, height=400)

    def draw(self):
        self.canvas.pack(fill=BOTH, expand=1)
        mainloop()

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.color == other.color

    def __str__(self):
        return f'Figure({self.__class__}, color: {self.color})'

class Rectangle(Figure):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def draw(self):
        x1, y1 = self.display_margin_left, self.display_margin_top
        x2, y2 = x1 + self.b, y1 + self.a
        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            outline='#ccc', fill=self.color, width=2,
        )
        super().draw()

    def __eq__(self, other):
        if super().__eq__(other):
            return {self.a, self.b} == {other.a, other.b}
        return False

class Square(Rectangle):
    def __init__(self, color, a):
        super().__init__(color, a, a)

class Circle(Figure):
    def __init__(self, color, r):
        super().__init__(color)
        self.r = r

    def draw(self):
        """
        TODO: calculate coordinates basing on `self.r`
        :return:
        """
        self.canvas.create_oval(10, 10, 80, 80, outline="#ccc",
                                fill=self.color, width=2)
        super().draw()

    def __eq__(self, other):
        if super().__eq__(other):
            return self.r == other.r
        return False

class Triangle(Figure):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    @property
    def circuit(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        """Heron"""
        p = 0.5 * self.circuit
        return math.sqrt(p * (p - self.a)*(p - self.b)*(p - self.c))

    def __eq__(self, other):
        if super().__eq__(other):
            return {self.a, self.b, self.c} == {other.a, other.b, other.c}
        return False

class FiguresList(list):

    def append(self, item):
        if not isinstance(item, Figure):
            # at this stage it could be `return False`
            raise TypeError(f'Object is not of type: {Figure}')
        if item in self:
            raise ValueError(f'Object already exists {item}')
        super().append(item)


if __name__ == '__main__':
    square = Square('#000', 2)
    print(square.color)
    print(square.a, square.area)
    rect = Rectangle('#fff', 20, 40)
    print(rect.color)
    print(rect.a, rect.area)
    rect.draw()
    circle = Circle('#fcc', 11)
    circle.draw()
    circle1 = Circle('#fcc', 11)
    circle2 = Circle('#fda', 10)

    print(circle == circle1)

    tri = Triangle('#fff', 20, 20, 30)

    figures = FiguresList([square, rect, circle])
    figures.append(circle2)
    print(circle2)
    print(figures)
    figures.append(circle1) # should raise exception