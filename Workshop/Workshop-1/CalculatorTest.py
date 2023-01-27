import unittest
import Calculator as calc
class TestCalc(unittest.TestCase):

# Happy Path Test
    def test010_Multiplication(self):
        x = 3
        y = -2
        expected = -6
        actual = calc.performMult(x, y)
        self.assertEqual(expected, actual, "bug in implementation. Result should be -6")


if __name__ == '__main__':
    unittest.main()


