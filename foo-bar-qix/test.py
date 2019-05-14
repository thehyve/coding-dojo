#!/usr/bin/env python3

import unittest
from fbq import compute

class FooBarQixTestCase(unittest.TestCase):

    def test_that_passing_one_results_in_one(self):
        result = compute('1')
        self.assertEqual(result, '1')

    def test_that_passing_two_results_in_two(self):
        result = compute('2')
        self.assertEqual(result, '2')

if __name__ == '__main__':
    unittest.main()
