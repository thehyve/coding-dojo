#!/usr/bin/env python3

import unittest
from fbq import compute

class FooBarQixTestCase(unittest.TestCase):

    def assertResultsIn(self, arg, expected):
        result = compute(arg)
        self.assertEqual(result, expected)

    def test_that_passing_one_results_in_one(self):
        self.assertResultsIn('1', '1')

    def test_that_passing_two_results_in_two(self):
        self.assertResultsIn('2', '2')

    def test_that_passing_six_results_in_Foo(self):
        self.assertResultsIn('6', 'Foo')

    def test_that_passing_nine_results_in_Foo(self):
        self.assertResultsIn('9', 'Foo')

if __name__ == '__main__':
    unittest.main()
