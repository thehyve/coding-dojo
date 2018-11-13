#!/usr/bin/env python3

import unittest
from arg_parser import parse_args

class ArgumentParserCase(unittest.TestCase):
    def test_that_logging_is_false_if_not_passed(self):
        """If there's no -l argument, value should be false."""
        # given
        arg_list = []
        schema = {'l': 'flag'}
        # when
        parsed_args = parse_args(schema, arg_list)
        # then
        self.assertFalse(parsed_args['l'])

    def test_that_logging_is_true_if_passed(self):
        """If there is an -l argument, value should be true."""
        # given
        arg_list = ['-l']
        schema = {'l': 'flag'}
        # when
        parsed_args = parse_args(schema, arg_list)
        # then
        self.assertTrue(parsed_args['l'])

if __name__ == '__main__':
    unittest.main()
