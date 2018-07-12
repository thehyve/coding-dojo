import fizbuz
import unittest

class TestFizBuz(unittest.TestCase):

    def test_first_element(self):
        fb = fizbuz.FizBuz()
        self.assertEqual(1, next(fb.get_generator()))

    def test_3rd_element(self):
        generator = fizbuz.FizBuz().get_generator()
        next(generator)
        next(generator)
        self.assertEqual("Fizz",next(generator))
        
    def test_length_is_100(self):
        generator = fizbuz.FizBuz().get_generator()
        generator_as_list = list(generator)
        self.assertEqual(100, len(generator_as_list))
        
    def test_buzz(self):
        generator = fizbuz.FizBuz().get_generator()
        generator_as_list = list(generator)
        self.assertEqual('Buzz', generator_as_list[4])
        
    def test_fizz_buzz(self):
        generator = fizbuz.FizBuz().get_generator()
        generator_as_list = list(generator)
        self.assertEqual('FizzBuzz', generator_as_list[14])
        

if __name__ == '__main__':
    unittest.main() # pragma: no cover

