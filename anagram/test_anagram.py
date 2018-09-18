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

    def test_that_multi_letter_word_is_its_own_anagram(self):
        word = 'hello'
        output = anagrams(word)
        self.assertIn(word, output)

    def test_that_some_multi_letter_words_have_more_than_one_anagram(self):
        word = 'stop'
        output = anagrams(word)
        self.assertTrue(len(list(output)) > 1)

    def test_that_nonword_is_not_a_valid_anagram_of_itself(self):
        word = 'hjko'
        output = anagrams(word)
        self.assertNotIn(word, output)

    def test_that_some_word_has_two_words_anagram(self):
        word = 'output'
        output = anagrams(word)
        self.assertIn(True, ((' ' in result) for result in output), 'jopa')

if __name__ == '__main__':
    unittest.main()
