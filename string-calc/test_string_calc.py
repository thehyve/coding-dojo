import unittest
from string_calc import add

class RomanNumeralsTest(unittest.TestCase):
	def test_add_empty_string(self):
		self.assertEqual('0', add(''))

	def test_add_one(self):
		self.assertEqual('1', add('1'))

	def test_add_two_ones(self):
		self.assertEqual('2', add('1,1'))

	def test_add_three_ones(self):
		self.assertEqual('3', add('1,1,1'))

	def test_that_add_splits_on_newlines(self):
		self.assertEqual('2', add('1\n1'))

if __name__ == '__main__':
    unittest.main() # pragma: no cover
