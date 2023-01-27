import unittest
import Calculator as calc
class TestCalc(unittest.TestCase):



# Analysis performMult(x, y)
# 
#   inputs:
#       x: number (int or float)
#       y: number (int or float)
#   
#   outputs:
#       side-effect: No State Change
#       returns: {x * y, "Must input two valid numbers (x, y)"}
#
# Regular Path Test
    def test010_IntegerMultiplication(self):
        x = 3
        y = -2
        expected = -6
        actual = calc.performMult(x, y)
        self.assertEqual(expected, actual, "bug in implementation. Result should be -6")
    
    def test020_FloatMultiplication(self):
        x = 2.345
        y = -6.3356
        expected = -14.856982
        actual = calc.performMult(x, y)
        self.assertEqual(expected, actual, "bug in implementation. Result should be -14.856982")
    
    def test030_IntFloatMultiplication(self):
        x = 2
        y = -12.356
        expected = -24.712
        actual = calc.performMult(x, y)
        self.assertEqual(expected, actual, "bug in implementation. Result should be -24.712")

# Error Path Test

    def test910_NonIntegerInputs(self):
        x = "X"
        y = "Y"
        expected = "Must input two valid numbers (x, y)"
        actual = calc.performMult(x, y)
        self.assertEqual(expected, actual, "bug in implementation. Result should be 'Must input two valid numbers (x, y)'")
    
    def test920_MissingInputs(self):
        expected = "Must input two valid numbers (x, y)"
        actual = calc.performMult()
        self.assertEqual(expected, actual, "bug in implementation. Result should be 'Must input two valid numbers (x, y)'")



if __name__ == '__main__':
    unittest.main()


