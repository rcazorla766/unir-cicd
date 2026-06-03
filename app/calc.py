import math

class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def subtract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def square_root(self, x):
        self.check_types(x, 0)
        if x < 0:
            raise TypeError("Cannot calculate square root of a negative number")

        return math.sqrt(x)
    
    def logarithm(self, x):
        self.check_types(x, 10)
        if x <= 0:
            raise TypeError("Logarithm is only defined for positive numbers and bases greater than 1")

        return math.log(x, 10)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
