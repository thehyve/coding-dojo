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

    def test_that_passing_three_results_in_FooFoo(self):
        self.assertResultsIn('3', 'FooFoo')

    def test_that_passing_four_results_in_four(self):
        self.assertResultsIn('4', '4')

    def test_that_passing_five_results_in_BarBar(self):
        self.assertResultsIn('5', 'BarBar')

    def test_that_passing_six_results_in_Foo(self):
        self.assertResultsIn('6', 'Foo')

    def test_that_passing_seven_results_in_QixQix(self):
        self.assertResultsIn('7', 'QixQix')

    def test_that_passing_eight_results_in_eight(self):
        self.assertResultsIn('8', '8')

    def test_that_passing_nine_results_in_Foo(self):
        self.assertResultsIn('9', 'Foo')

    def test_that_passing_ten_results_in_Bar(self):
        self.assertResultsIn('10', 'Bar')


if __name__ == '__main__':
    unittest.main()
