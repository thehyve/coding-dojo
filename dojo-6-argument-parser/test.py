#!/usr/bin/env python3

import unittest
from arg_parser import parse_args

class ArgumentParserCase(unittest.TestCase):
    def test_that_flag_is_false_if_not_passed(self):
        """If there's no -l argument, value should be false."""
        # given
        arg_list = []
        schema = {'l': 'flag'}
        # when
        parsed_args = parse_args(schema, arg_list)
        # then
        self.assertFalse(parsed_args['l'])

    def test_that_flag_is_true_if_passed(self):
        """If there is an -l argument, value should be true."""
        # given
        arg_list = ['-l']
        schema = {'l': 'flag'}
        # when
        parsed_args = parse_args(schema, arg_list)
        # then
        self.assertTrue(parsed_args['l'])

    def test_that_flag_is_false_when_other_flag_passed(self):
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
        # then
        with self.assertRaises(ValueError):
        # when
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

    def test_that_integer_param_is_parsed_to_int(self):
        # given
        arg_list = ['-p', '8080']
        schema = {'p': 'int'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r['p'], 8080)

    def test_that_integer_is_0_if_value_not_present(self):
        # given
        arg_list = ['-l']
        schema = {'p': 'int', 'l': 'flag'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r['p'], 0)

    def test_that_invalid_integer_raises_value_error(self):
        # given
        arg_list = ['-p', 'pi']
        schema = {'p': 'int'}
        # when, then
        with self.assertRaises(ValueError):
            _ = parse_args(schema, arg_list)

    def test_that_negative_ints_are_parsed_as_ints(self):
        # given
        arg_list = ['-p', '-3']
        schema = {'p': 'int'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r['p'], -3)

    def test_that_double_digit_negative_int_is_parsed(self):
        # given
        arg_list = ['-p', '-13']
        schema = {'p': 'int'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r['p'], -13)

    def test_that_string_values_get_parsed(self):
        # given
        arg_list = ['-s', 'abc']
        schema = {'s': 'str'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r['s'], 'abc')

    def test_not_provided_str_arg_defaults_to_empty_string(self):
        # given
        arg_list = []
        schema = {'s': 'str'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r['s'], '')

    def test_that_flags_can_have_digits_as_names(self):
        # given
        arg_list = ['-1']
        schema = {'1': 'flag'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertTrue(r['1'])

    def test_that_arguments_have_digit_as_name_and_value(self):
        # given
        arg_list = ['-1', '2']
        schema = {'1': 'int'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r['1'], 2)

    def test_that_negative_num_args_have_digits_as_name(self):
        # given
        arg_list = ['-1', '-12']
        schema = {'1': 'int'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r['1'], -12)

    def test_that_multiple_flags_can_have_digits_as_names(self):
        # given
        arg_list = ['-1', '-2']
        schema = {'1': 'flag', '2': 'flag'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertTrue(r['1'])
        self.assertTrue(r['2'])

    def test_that_schema_validation_works_with_numeric_arg_names(self):
        # given
        arg_list = ['-1', '-2', '-3']
        schema = {'1': 'flag', '2': 'flag'}
        # when
        # then
        with self.assertRaises(ValueError):
            _ = parse_args(schema, arg_list)

    def test_that_unknown_options_are_detected_after_options_that_take_arguments(self):
        # given
        arg_list = ['-p', '3', '-l']
        schema = {'p': 'int'}
        # when, then
        with self.assertRaises(ValueError):
            _ = parse_args(schema, arg_list)

    def test_that_positional_args_are_collected(self):
        # given
        arg_list = ['1']
        schema = {}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r.positional, ['1'])

    def test_that_positional_args_that_follow_a_flag_are_collected(self):
        # given
        arg_list = ['-s', '1']
        schema = {'s': 'flag'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r.positional, ['1'])

    def test_that_a_flag_followed_by_a_positional_is_collected(self):
        # given
        arg_list = ['-s', '1']
        schema = {'s': 'flag'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertTrue(r['s'])

    def test_that_a_positional_that_follows_int_arg_is_collected(self):
        # given
        arg_list = ['-i', '2', '1']
        schema = {'i': 'int'}
        # when
        r = parse_args(schema, arg_list)
        # then
        self.assertEqual(r.positional, ['1'])


if __name__ == '__main__':
    unittest.main()
