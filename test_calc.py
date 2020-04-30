import unittest
import calc

# Run by: $ python -m unittest test_calc

# class that inherits from unittest.TestCase
class TestCalc(unittest.TestCase):
    def test_add(self): # name needs to be test_<function_to_be_tested>
        # List of the avaiable assert methods: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
        self.assertEqual( calc.add(10, 5), 15)
        self.assertEqual( calc.add(-1, 1), 0)
        self.assertEqual( calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual( calc.subtract(10, 5), 5)
        self.assertEqual( calc.subtract(-1, 1), -2)
        self.assertEqual( calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual( calc.multiply(10, 5), 50)
        self.assertEqual( calc.multiply(-1, 1), -1)
        self.assertEqual( calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual( calc.divide(10, 5), 2)
        self.assertEqual( calc.divide(11, 5), 2.2)
        self.assertEqual( calc.divide(-1, 1), -1)
        self.assertEqual( calc.divide(-1, -1), 1)

        self.assertRaises(ValueError, calc.divide, 10, 0) # test that a ValueError is produced if 10 is divided by 0
        # self.assertRaises(ValueError, calc.divide, 10, 2) # test that a ValueError is produced if 10 is divided by 0

        # alternatively, test the Exception using a "context manager"
        # with self.assertRaises(ValueError):
        #     calc.divide(10, 0)


# allows to run the tests using simply $ python test_calc.py
if __name__ == "__main__": 
    unittest.main()

