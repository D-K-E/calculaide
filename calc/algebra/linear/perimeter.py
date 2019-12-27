# Simple calculator for perimeters of different shapes intended for educative use
# author: Kaan Eraslan
# license: see, LICENSE

from calc.basecalc import Calculator
from typing import Callable, List
import inspect


class TrianglePerimCalculator(Calculator):
    def __init__(self, sides):
        self.sides = sides
        self.exp = """
        ======================
        Perimeter of Triangle
        ======================

               A
              / \
             /   \
            /     \
           B-------C

        Basically the perimeter of triangle is |AB| + |AC| + |BC|
        """
        self.formula = "|AB| + |BC| + |AC| = P_{triangle}"

    def show_formula(self):
        print(self.formula)

    def show_explanation(self):
        print(self.exp)

    def perimeter(self):
        return sum(self.sides)

    def result(self):
        self.show_explanation()
        self.show_formula()
        print("\nHere is our implementation:\n")
        print(inspect.getsource(self.perimeter))
        print("\nGives the following result:\n")
        print(str(self.perimeter()))


class RectanglePerimeterCalculator(Calculator):
    "Rectangle perimeter calculator"

    def __init__(self, width: float, height: float):
        self.w = width
        self.h = height
        self.exp = """
        ======================
        Perimeter of Rectangle
        ======================

        A------------D
        |            |
        |            | width
        |            |
        B------------C
             height

        Perimeter of Rectangle is |AB| + |BC| + |CD| + |DA|
        which can also be expressed as 2 * width + 2 * height
        """
        self.formula = "2 * width + 2 * height"

    def show_formula(self):
        print(self.formula)

    def show_explanation(self):
        print(self.exp)

    def perimeter(self):
        return 2 * self.w + self.h * 2

    def result(self):
        self.show_explanation()
        self.show_formula()
        print("\nHere is our implementation:\n")
        print(inspect.getsource(self.perimeter))
        print("\nGives the following result:\n")
        print(str(self.perimeter()))


def main():
    print("Welcome to Perimeter Calculator")
    choice = input(
        """
            Choose your calculator:

                - r -> rectangle
                - t -> triangle

            """
    )
    if choice == "r":
        pass
    elif choice == "t":
        pass


if __name__ == "__main__":
    main()
