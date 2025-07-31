import unittest
import cal

class TestCal(unittest.TestCase):
    def test_add(self):
        result = cal.add(10,5)
        self.assertEqual(result, 15)
    def test_subtract(self):
        result = cal.subtract(10,5)
        self.assertEqual(result,5)
    def test_divide(self):
        result = cal.divide(10,2)
        self.assertEqual(result,5)
    def test_multiply(self):
        result = cal.multiply(10,5)
        self.assertEqual(result,50)

if __name__ == '__main__':
    unittest.main()