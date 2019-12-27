# Simple calculator for differentials intended for educative use
# author: Kaan Eraslan
# license: see, LICENSE

import math

from calc.basecalc import Calculator
from typing import Callable, List
import inspect


class D1DiffCalculator(Calculator):
    "Differential calculator for single dimension"

    def __init__(self, param, diff_step):
        "constructor"
        self.step = diff_step
        self.param = param
        self.formula = """
        f'(x1) = (f(x2) - f(x1)) / (x2 - x1) where (x2-x1) decreases into 0"""
        self.exp = """
        ==============
        Differentials
        ==============

        Differentials measure the rate of change and
        respond to the following question:

        What is the difference between the current instant and the instant
        before?

        This question supposes several things under the hood:
            - Current instant and the instant before are comparable.
            - The same function can be applied to both instances.

        Here is the formula: {0}

        Terms: 
            - f(x2): corresponds to current instant
            - f(x1): corresponds to instant before
            - (x2 - x1): is the distance between current instant and instant
              before, it can be as small as possible, it is almost 0.
        """.format(
            self.formula
        )

    def f(self, x):
        "a simple function "
        return x ** 2 + 7

    def show_formula(self):
        print(self.formula)
        print("\nHere is the f we are using: \n")
        print(inspect.getsource(self.f))

    def show_explanation(self):
        print(self.exp)

    def de(self, fn, x, step):
        "take derivative of a function with respect to given variable and step"
        instant_before = fn(x)
        current_instant = fn(x + step)
        result = (current_instant - instant_before) / step
        return result

    def derivative_of_f(self):
        instant_before = self.f(self.param)
        current_instant = self.f(self.param + self.step)
        result = (current_instant - instant_before) / self.step
        return result

    def result(self):
        self.show_explanation()
        self.show_formula()
        print("\nHere is our implementation:\n")
        print(inspect.getsource(self.derivative_of_f))
        print("\nGives the following result:\n")
        print(str(self.derivative_of_f()))


class D1Rules(D1DiffCalculator):
    def __init__(self, param, diff_step):
        super().__init__(param, diff_step)
        self.add_rule = """
        k(x) = f(x) + g(x) 

        k'(x) = f'(x) + g'(x)
        """
        self.sub_rule = """
        k(x) = f(x) - g(x) 

        k'(x) = f'(x) - g'(x)
        """
        self.prod_rule = """
        k(x) = f(x)*g(x)

        k'(x) = f'(x)*g(x) + f(x)*g'(x)
        """
        self.div_rule = """
        k(x) = f(x) / g(x)

        k'(x) = [f'(x)g(x) - f(x)g'(x)] / g(x) * g(x)
        """
        self.chain_rule = """
        k(x) = f( g(x) )

        k'(x) = f'(g(x)) * g'(x)
        """

    def g(self, x):
        "a simple function"
        return x ** 3 + 2

    def add_fn(self, x):
        return self.f(x) + self.g(x)

    def deriv_add_fn(self, x, step):
        return self.de(self.f, x, step) + self.de(self.g, x, step)

    def sub_fn(self, x):
        return self.f(x) - self.g(x)

    def de_sub_fn(self, x, step):
        return self.de(self.f, x, step) - self.de(self.g, x, step)

    def chain_fn(self, x):
        return self.f(self.g(x))

    def de_chain_fn(self, x, step):
        d_g = self.de(self.g, x, step)
        gres = self.g(x)
        d_f_g = self.de(self.f, gres, step)
        return d_g * d_f_g

    def prod_fn(self, x):
        return self.f(x) * self.g(x)

    def de_prod_fn(self, x, step):
        d_g = self.de(self.g, x, step)
        d_f = self.de(self.f, x, step)
        gres = self.g(x)
        fres = self.f(x)
        return (d_f * gres) + (fres * d_g)

    def div_fn(self, x):
        return self.f(x) / self.g(x)

    def de_div_fn(self, x, step):
        d_g = self.de(self.g, x, step)
        d_f = self.de(self.f, x, step)
        gres = self.g(x)
        fres = self.f(x)
        p1 = d_f * gres
        p2 = fres * d_g
        return (p1 - p2) / (d_g * d_g)

    def show_rule(self, rname: str, rule, kx, d_kx, res1, res2):
        print("\n{0} Demonstration".format(rname.capitalize()))
        print("---------------------------\n\n")
        print("Here is the {0}: ".format(rname))
        print(rule, "\n\n")
        print("Here is the body of k(x):\n")
        print(inspect.getsource(kx))
        print("Here is the body of k'(x):\n")
        print(inspect.getsource(d_kx))
        print("Let's see if the rule holds: ")
        print(
            "Here is the result of the derivative of k(x) computed directly: ",
            str(res2),
        )
        print(
            "Here is the result of k(x) computed in parts as seen at right of =: ",
            str(res1),
        )

    def show_addition_rule(self):
        result1 = self.de(self.add_fn, self.param, self.step)
        result2 = self.deriv_add_fn(self.param, self.step)
        self.show_rule(
            rname="addition rule",
            rule=self.add_rule,
            kx=self.add_fn,
            d_kx=self.deriv_add_fn,
            res1=result1,
            res2=result2,
        )

    def show_subtraction_rule(self):
        result1 = self.de(self.sub_fn, self.param, self.step)
        result2 = self.de_sub_fn(self.param, self.step)
        self.show_rule(
            rname="subtraction rule",
            rule=self.sub_rule,
            kx=self.sub_fn,
            d_kx=self.de_sub_fn,
            res1=result1,
            res2=result2,
        )

    def show_chain_rule(self):
        result2 = self.de_chain_fn(self.param, self.step)
        result1 = self.de(self.chain_fn, self.param, self.step)
        self.show_rule(
            rname="chain rule",
            rule=self.chain_rule,
            kx=self.chain_fn,
            d_kx=self.de_chain_fn,
            res1=result1,
            res2=result2,
        )

    def show_product_rule(self):
        result1 = self.de(self.prod_fn, self.param, self.step)
        result2 = self.de_prod_fn(self.param, self.step)
        self.show_rule(
            rname="product rule",
            rule=self.prod_rule,
            kx=self.prod_fn,
            d_kx=self.de_prod_fn,
            res1=result1,
            res2=result2,
        )

    def show_div_rule(self):
        result1 = self.de(self.div_fn, self.param, self.step)
        result2 = self.de_div_fn(self.param, self.step)
        self.show_rule(
            rname="division rule",
            rule=self.div_rule,
            kx=self.div_fn,
            d_kx=self.de_div_fn,
            res1=result1,
            res2=result2,
        )


def main():
    print("Welcome to simple differential calculator")
    param = input("Enter a floating number [Ex. 12.2, 42.1, etc]: ")
    param = float(param)
    print("Using 0.0001 as a step value")
    calc = D1DiffCalculator(param, 0.001)
    calc.result()
    cont = input(
        """
    Would you like to learn about rules of derivative as well ?
    Available choices are:
        - a: addition rule
        - s: subtraction rule
        - p: product rule
        - d: division rule
        - c: chain rule
        - q: quit application
    """
    )
    if cont == "q":
        return 0
    ruler = D1Rules(param, 0.0001)
    if cont == "a":
        ruler.show_addition_rule()
    elif cont == "s":
        ruler.show_subtraction_rule()
    elif cont == "c":
        ruler.show_chain_rule()
    elif cont == "d":
        ruler.show_div_rule()
    elif cont == "p":
        ruler.show_product_rule()


if __name__ == "__main__":
    main()
