import unittest
from anagrams import anagrams

class AnagramTests(unittest.TestCase):
    def test_that_one_letter_word_is_its_own_only_anagram(self):
        word = 'a'
        output = anagrams(word)
        self.assertEqual(next(output), 'a')
        with self.assertRaises(StopIteration):
            next(output)

    def test_that_diff_one_letter_word_is_its_own_only_anagram(self):
        word = 'I'
        output = anagrams(word)
        self.assertEqual(next(output), 'I')
        with self.assertRaises(StopIteration):
            next(output)

    def test_that_nonword_has_no_anagram(self):
        word = 'b'
        output = anagrams(word)
        with self.assertRaises(StopIteration):
            next(output)

if __name__ == '__main__':
    unittest.main()
