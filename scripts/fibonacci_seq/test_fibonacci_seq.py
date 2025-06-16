import unittest
"""
Unit tests for the `fibonacci_recursive` function from the `fibonacci_seq` module.
Test Cases:
-----------
- test_zero: Verifies that input 0 returns an empty list.
- test_one: Verifies that input 1 returns a list with a single Fibonacci number [0].
- test_two: Verifies that input 2 returns the first two Fibonacci numbers [0, 1].
- test_five: Checks the first five Fibonacci numbers.
- test_ten: Checks the first ten Fibonacci numbers.
- test_negative: Ensures negative input returns an empty list.
- test_large: Checks correctness for a larger sequence (first 20 Fibonacci numbers).
- test_non_integer: Ensures a TypeError is raised for string input.
- test_float_input: Ensures a TypeError is raised for float input.
- test_list_input: Ensures a TypeError is raised for list input.
- test_none_input: Ensures a TypeError is raised for None input.
- test_bool_input: Verifies that boolean inputs are handled as integers (True as 1, False as 0).
Usage:
------
Run this test suite to validate the correctness and robustness of the `fibonacci_recursive` implementation.
"""
from fibonacci_seq import fibonacci_recursive

class TestFibonacciRecursive(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibonacci_recursive(0), [])

    def test_one(self):
        self.assertEqual(fibonacci_recursive(1), [0])

    def test_two(self):
        self.assertEqual(fibonacci_recursive(2), [0, 1])

    def test_five(self):
        self.assertEqual(fibonacci_recursive(5), [0, 1, 1, 2, 3])

    def test_ten(self):
        self.assertEqual(fibonacci_recursive(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_negative(self):
        self.assertEqual(fibonacci_recursive(-5), [])

    def test_large(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        self.assertEqual(fibonacci_recursive(20), expected)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            fibonacci_recursive("five")

    def test_float_input(self):
        with self.assertRaises(TypeError):
            fibonacci_recursive(5.5)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            fibonacci_recursive([5])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            fibonacci_recursive(None)

    def test_bool_input(self):
        # True is treated as 1, False as 0 in Python, so check for that
        self.assertEqual(fibonacci_recursive(True), [0])
        self.assertEqual(fibonacci_recursive(False), [])

if __name__ == '__main__':
    unittest.main()