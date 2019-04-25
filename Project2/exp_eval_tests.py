#
#Kelsey Deuth
#
#04/23/19
#
#Project2
#Section 11
#this code tests solutions of prexif, infix, and postfix expressions using stack arrays in exp_eval.py

# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        try:
            postfix_eval("4 4 5 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("( 2 + 3 ) / 2"), "2 3 + 2 /")
        self.assertEqual(infix_to_postfix("( 2 + 4 / 3 ) - 4 ** 2"), "2 4 3 / + 4 2 ** -")
        self.assertEqual(infix_to_postfix("( 4 / 2 + 3 ) - 4 ** 2"), "4 2 / 3 + 4 2 ** -")
        self.assertEqual(infix_to_postfix("( 4 / 2 * 3 + 1 ) - 4"), "4 2 / 3 * 1 + 4 -")
        
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_do_math(self):
        self.assertEqual(do_math('+', 1, 1), 2)
        self.assertEqual(do_math('-', 2, 1), 1)
        self.assertEqual(do_math('*', 2, 1), 2)
        self.assertEqual(do_math('/', 2, 1), 2)
        with self.assertRaises(ValueError):  #checks for exception
            self.assertEqual(do_math('/', 2, 0))
        self.assertEqual(do_math('**', 2, 2), 4)
        self.assertEqual(do_math('>>', 2, 3), 0)
        self.assertEqual(do_math('<<', 2, 3), 16)
        try:
            do_math('>>', 2.0, 3.0)
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            do_math('<<', 2.0, 3.0)
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test1(self):
        stack1 = Stack(1)
        stack1.push(2)
        self.assertFalse(stack1.is_empty())
        with self.assertRaises(IndexError):  #checks for exception
            stack1.push(1)

    def test2(self):
        stack2 = Stack(5)
        stack2.push(3)
        stacktest = Stack(0)
        self.assertEqual(stack2.pop(), 3)
        with self.assertRaises(IndexError):  #checks for exception
            stacktest.pop()
        with self.assertRaises(IndexError):  #checks for exception
            stacktest.peek()




if __name__ == "__main__":
    unittest.main()

