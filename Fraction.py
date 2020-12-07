class Fraction(object):
    """docstring"""

    def __init__(self, numerator, denominator):
        """Constructor"""
        self.__numerator = numerator
        self.__denominator = denominator

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def set_numerator(self, numerator):
        self.__numerator = numerator

    def set_denominator(self, denominator):
        self.__denominator = denominator

    def numbers_sum(self):
        return self.get_numerator() + self.get_denominator()

    def numbers_multiplication(self):
        return self.get_numerator() * self.get_denominator()

    def numbers_subtraction(self):
        return self.get_numerator() - self.get_denominator()

    def numbers_division(self):
        return self.get_numerator() / self.get_denominator()

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self, p):
        """
        Drive the car
        """
        return p
