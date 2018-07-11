import unittest
import roman

class RomanTest(unittest.TestCase):
	"""I + I = II"""
	def test_one_plus_one(self):
		self.assertEqual("II", roman.Roman().add("I", "I"))

	def test_one_plus_two(self):
		self.assertEqual("III", roman.Roman().add("I", "II"))

	def test_two_plus_two(self):
		self.assertEqual("IV", roman.Roman().add("II", "II"))

	def test_one_plus_five(self):
		self.assertEqual("VI", roman.Roman().add("I", "V"))

	def test_three_plus_three(self):
		self.assertEqual("VI", roman.Roman().add("III", "III"))

	def test_two_plus_five(self):
		self.assertEqual("VII", roman.Roman().add("II", "V"))


if __name__ == '__main__':
    unittest.main() # pragma: no cover
