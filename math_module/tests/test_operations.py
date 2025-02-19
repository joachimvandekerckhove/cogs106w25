import unittest
from mathops.operations import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a Calculator instance before each test."""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 20), -10)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(3, 2), 1.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_history(self):
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)

if __name__ == '__main__':
    unittest.main()
