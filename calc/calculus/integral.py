# Simple calculator for integrals intended for educative use
# author: Kaan Eraslan
# license: see, LICENSE

import math

from calc.basecalc import Calculator
from typing import Callable, List
import inspect


class D1IntegralCalculator(Calculator):
    "1D integral calculator"

    def __init__(self, upper_bound, lower_bound, step):
        ""
        self.ub = upper_bound
        self.lb = lower_bound
        self.f = fn
        self.step = step
        self.exp = """
        =========
        Integrals
        =========

        Integrals measure the area under the curve of a function that is 
        differentiable.

        This means that:
            - We know the global behaviour of the function
        """

        pass


def main():
    print("Welcome to simple differential calculator")
    param = input("Enter a floating number [Ex. 12.2, 42.1, etc]: ")
    param = float(param)
    print("Using 0.0001 as a step value")
    calc = D1DiffCalculator(param, 0.001)
    calc.result()


if __name__ == "__main__":
    main()
