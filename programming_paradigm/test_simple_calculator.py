import unittest
from simple_calculator import SimpleCalculator

class Testsimple_calculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add(self):
        result = self.calc.add(10,5)
        self.assertEqual(result,15)
    def test_subtract(self):
        result = self.calc.subtract(10,5)
        self.assertEqual(result,5)
    def test_multiply(self):
        result = self.calc.multiply(10,5)
        self.assertEqual(result,50)
    def test_divide(self):
        result = self.calc.divide(10,5)
        self.assertEqual(result,2)
if __name__ == '__main__':
    unittest.main()
    