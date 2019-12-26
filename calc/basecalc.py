# Simple calculator interface to be implemented by all calculators
# author: Kaan Eraslan
# license: see, LICENSE

from abc import ABC, abstractmethod


class Calculator(ABC):
    "A base class for all calculators"

    @abstractmethod
    def show_formula(self):
        raise NotImplementedError

    @abstractmethod
    def show_explanation(self):
        raise NotImplementedError

    @abstractmethod
    def result(self):
        raise NotImplementedError
