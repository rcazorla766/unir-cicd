import unittest
import pytest

from app.calc import Calculator


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
#-------Test cases where it works correctly------------------------------------------------------

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(9, self.calc.add(5, 4))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.subtract(2, 2))
        self.assertEqual(1, self.calc.subtract(5, 4))
        self.assertEqual(4, self.calc.subtract(2, -2))
        self.assertEqual(-4, self.calc.subtract(-2, 2))
        self.assertEqual(1, self.calc.subtract(1, 0))
    
    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(6, self.calc.multiply(3, 2))
        self.assertEqual(4, self.calc.multiply(-2, -2))
        self.assertEqual(-4, self.calc.multiply(2, -2))
        self.assertEqual(-4, self.calc.multiply(-2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(-1, self.calc.divide(2, -2))
        self.assertEqual(-1, self.calc.divide(-2, 2))
        self.assertEqual(1, self.calc.divide(-2, -2))
    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(0.25, self.calc.power(-2, -2))
        self.assertEqual(4, self.calc.power(-2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(0, 0))

    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(0, self.calc.square_root(0))
        self.assertEqual(3, self.calc.square_root(9))

    def test_logarithm_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.logarithm(10))
        self.assertEqual(2, self.calc.logarithm(100))
        self.assertEqual(0, self.calc.logarithm(1))

    #--------------Test cases where it fails (by invalid input or invalid operations)-----------------

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
    
    def test_subtract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.subtract, "2", 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, "2")
        self.assertRaises(TypeError, self.calc.subtract, "2", "2")
        self.assertRaises(TypeError, self.calc.subtract, None, 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, None)
        self.assertRaises(TypeError, self.calc.subtract, object(), 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, object())
    
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
    
    def test_square_root_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.square_root, "4")
        self.assertRaises(TypeError, self.calc.square_root, None)
        self.assertRaises(TypeError, self.calc.square_root, object())
    
    def test_square_root_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.square_root, -1)
        self.assertRaises(TypeError, self.calc.square_root, -100)
        self.assertRaises(TypeError, self.calc.square_root, -0.0001)

    def test_logarithm_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.logarithm, "10")
        self.assertRaises(TypeError, self.calc.logarithm, None)
        self.assertRaises(TypeError, self.calc.logarithm, object())
    
    def test_logarithm_method_fails_with_non_positive_parameter(self):
        self.assertRaises(TypeError, self.calc.logarithm, 0)
        self.assertRaises(TypeError, self.calc.logarithm, -1)
        self.assertRaises(TypeError, self.calc.logarithm, -100)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
