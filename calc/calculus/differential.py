# Simple calculator for differentials intended for educative use
# author: Kaan Eraslan
# license: see, LICENSE

import math


class DiffCalculator:
    def __init__(self, param: float, diff_step: float, fn=lambda x, y: x + y):
        "constructor"
        self.fn = fn
        self.step = diff_step
        self.param = param
        self.exp = """
        """


def main():
    pass


if __name__ == "__main__":
    main()
