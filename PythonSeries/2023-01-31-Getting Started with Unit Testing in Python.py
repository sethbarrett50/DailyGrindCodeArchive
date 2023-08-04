# The unittest module is a built-in Python library that allows for the creation and execution of unit tests.
# Here are some of the most commonly used methods in the unittest module:

'''assertEqual(a, b): This method checks if the values of a and b are equal. If they are not, it raises an AssertionError.'''
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

'''assertTrue(x): This method checks if the value of x is True. If it is not, it raises an AssertionError.'''
import unittest

def is_even(x):
    return x % 2 == 0

class TestIsEven(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))

'''assertRaises(exception, function, *args): This method checks if the specified function raises the specified exception when called with the specified args. If the function does not raise the exception, it raises an AssertionError.'''
import unittest

def divide(a, b):
    return a / b

class TestDivide(unittest.TestCase):

    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

'''setUp() and tearDown(): These methods are run before and after each test method in the test case, respectively. They can be used to set up any required resources or clean up after a test.'''
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.string = "hello world"

    def test_upper(self):
        self.assertEqual(self.string.upper(), "HELLO WORLD")

    def test_isupper(self):
        self.assertTrue(self.string.upper().isupper())

    def tearDown(self):
        del self.string