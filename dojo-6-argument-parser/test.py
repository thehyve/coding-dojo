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

    def test_that_false_returned_when_arg_not_provided_but_args_not_empty(self):
        # given
        arg_list = ['-l']
        schema = {'p':'flag', 'l':'flag'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertFalse(r['p'])

    def test_that_fails_in_case_arg_not_in_schema(self):
        """If there is an -l argument, but it is not in schema then fail."""
        # given
        arg_list = ['-l']
        schema = {'p':'flag'}
        # when
        with self.assertRaises(ValueError):
        # then
            parse_args(schema, arg_list)

    def test_that_other_letter_works(self):
        """Parser has to work for arbitrary flag letter."""
        # given
        arg_list = ['-p']
        schema = {'p':'flag'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertTrue(r['p'])

if __name__ == '__main__':
    unittest.main()
