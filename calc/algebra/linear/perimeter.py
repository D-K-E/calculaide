# Simple calculator for perimeters of different shapes intended for educative use
# author: Kaan Eraslan
# license: see, LICENSE

from calc.basecalc import Calculator
from typing import Callable, List
import inspect


class PerimeterCalculator(Calculator):
    def perimeter(self):
        raise NotImplementedError

    def show_formula(self):
        print(self.formula)

    def show_explanation(self):
        print(self.exp)

    def result(self):
        self.show_explanation()
        self.show_formula()
        print("\nHere is our implementation:\n")
        print(inspect.getsource(self.perimeter))
        print("\nGives the following result:\n")
        print(str(self.perimeter()))


class TrianglePerimCalculator(PerimeterCalculator):
    def __init__(self, sides: List[float]):
        self.side1 = sides[0]
        self.side2 = sides[1]
        self.side3 = sides[2]
        self.exp = """
        ======================
        Perimeter of Triangle
        ======================

               A
              / \\
             /   \\
            /     \\
           B-------C

        Basically the perimeter of triangle is |AB| + |AC| + |BC|
        """
        self.formula = "|AB| + |BC| + |AC| = P_{triangle}"

    def perimeter(self):
        result = self.side1 + self.side2 + self.side3
        return result


class SquarePerimeterCalculator(PerimeterCalculator):
    "Square perimeter calculator"

    def __init__(self, side: float):
        self.side = side
        self.exp = """
        ======================
        Perimeter of Square
        ======================

        A-------D
        |       |
        |       | side
        |       |
        B-------C
           side

        Perimeter of Square is |AB| + |BC| + |CD| + |DA|
        which can also be expressed as 4 * side
        """
        self.formula = "4 * side"

    def perimeter(self):
        return 4 * self.side


class RectanglePerimeterCalculator(PerimeterCalculator):
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

    def perimeter(self):
        return 2 * self.w + self.h * 2


class RhombusPerimeterCalculator(SquarePerimeterCalculator):
    "Compute rhombus perimeter"

    def __init__(self, side: float):
        super().__init__(side)
        self.exp = """
        =====================
        Perimeter of Rhombus
        =====================
          A 
          /\\
         /  \ side 
       B/    \ D
        \    /
         \  / side
          \/
          C

        Perimeter of Rhombus is |AB| + |BC| + |CD| + |DA|
        which can also be expressed as 4 * side
        """


class ParallelogramPerimeterCalculator(PerimeterCalculator):
    def __init__(self, horizontal_side: float, vertical_side: float):
        self.hside = horizontal_side
        self.vside = vertical_side
        self.exp = """
        ===========================
        Perimeter of Parallelogram
        ===========================

                   hside
              A ______________ D
               /             /
              /             / vside
             /             /
          B /_____________/ C

        Perimeter of Parallelogram is |AB| + |BC| + |CD| + |DA|
        which can also be expressed as 2 * vside + 2 * hside

        """
        self.formula = "2 * hside + 2 * vside"

    def perimeter(self):
        return 2 * self.hside + 2 * self.vside


class ClosedPolygonPerimeterCalculator(PerimeterCalculator):
    "Compute closed shaped polygon"

    def __init__(self, diff_list: List[float]):
        self.dlist = diff_list
        self.formula = "\sum_{i=1}^{k=(number of sides)} distance_i"
        self.exp = """
        =============================
        Perimeter of a Closed Polygon
        =============================
                 
                    J______________ I
                    /              \\
                  A/                \ H
                  |      ____       / 
                  |     /D  E\     /
                  |____/      \___/
                  B    C      F    G


        Perimeter of Closed Polygon is 
        |AB| + |BC| + |CD| + |DE| + |EF| + |FG| + |GH| + |HI| + |IJ| + |JA|

        which can be briefly expressed as

        .. math::

            \sum_{i=1}^{k=number of sides} d_i where

            d_i \in D = {f(x_1, x_2), f(x_2, x_3), ..., f(x_j, x_{j+1})}
            x_j \in Ordered set of Polygon Corners = {A, B, C, D, ... }
            f(x_j, x_{j+1}) = |x_j - x_{j+1}|

        """

    def perimeter(self):
        result = 0
        for absolute_difference_between_two_corners in self.dlist:
            result = result + absolute_difference_between_two_corners
        return result


class CirclePerimeterCalculator(Calculator):
    "Perimeter of a circle"
    def __init__(self, radius: float):
        self.r = radius
        self.exp = """
        ====================
        Perimeter of Circle
        ====================

        Perimeter of a circle is approximated by the use of regular polygons.
        It is considered as the limit of the perimeter of a regular polygon
        with infinite sides.

        """


def main():
    print("Welcome to Perimeter Calculator")
    choice = input(
        """
            Choose your calculator:

                - r -> rectangle
                - t -> triangle
                - s -> square
                - rh -> rhombus
                - p -> parallelogram
                - cp -> closed polygon

            """
    )
    if choice == "t":
        sides = input("Enter sides for triangle separated by comma Ex. 1.7,5.3,3.0: ")
        sides = list(map(float, sides.split(",")))
        calc = TrianglePerimCalculator(sides)
    elif choice == "r":
        sides = input(
            "Enter width and height for rectangle separated by comma Ex. 1.7,5.3: "
        )
        sides = list(map(float, sides.split(",")))
        calc = RectanglePerimeterCalculator(width=sides[0], height=sides[1])
    elif choice == "s":
        side = input("Enter a side for square: ")
        side = float(side)
        calc = SquarePerimeterCalculator(side)
    elif choice == "rh":
        side = input("Enter a side for rhombus: ")
        side = float(side)
        calc = RhombusPerimeterCalculator(side)
    elif choice == "p":
        sides = input(
            "Enter horizontal and vertical side length for parallelogram"
            " separated by comma Ex. 1.7,5.3: "
        )
        sides = list(map(float, sides.split(",")))
        calc = ParallelogramPerimeterCalculator(
            horizontal_side=sides[0], vertical_side=sides[1]
        )
    elif choice == "cp":
        sides = input(
            "Enter an ordered list of distances between corners of polygon"
            " separated by comma Ex. 1.7,5.3,2.3,65.2,23.5,...: "
        )
        sides = list(map(float, sides.split(",")))
        calc = ClosedPolygonPerimeterCalculator(sides)
    else:
        calc = None
        raise ValueError("Unknown choice: " + choice)
    calc.result()


if __name__ == "__main__":
    main()
