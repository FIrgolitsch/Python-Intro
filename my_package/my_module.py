from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    """
    This is an abstract class that defines a method that must be implemented by subclasses.
    """

    @abstractmethod
    def print_the_thing(self):
        """
        This method must be implemented by subclasses.

        :return: None
        """
        pass


class MyClass(MyAbstractClass):
    """
    This is a subclass of MyAbstractClass that implements the print_the_thing method.
    """

    def print_the_thing(self):
        """
        This method prints "The Thing".

        :return: None
        """
        print("The Thing")


def my_sum_function(a: int | float, b: int | float) -> int | float:
    """
    This function returns the sum of two numbers.

    :param a: number a
    :type a: int | float
    :param b: number b
    :type b: int | float
    :return: sum of a and b
    :rtype: int | float
    """
    return a + b


def my_non_top_level_function(text: str) -> None:
    """
    This function prints the input text.

    :param text: text to print
    :type text: str
    :return: None
    """
    print(str(text))


def my_divide_by_zero_function(number: float | int) -> float | int:
    """
    This function divides a number by zero.

    :param number: number to divide by zero
    :type number: double|int
    :return: division result
    :rtype: double|int
    """
    if number == 15:
        raise ValueError("Number cannot be 15")
    return number / 0
