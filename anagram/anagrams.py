from pathlib import Path
from itertools import permutations


def anagrams(word, n_words=1):
    yield from get_anagrams_in_language(word, n_words, read_english_words())

def get_anagrams_in_language(word, n_words, language_words):
    spaces_to_add = (n_words-1)*' '
    permutation_input = word + spaces_to_add
    all_permutations = {''.join(tuple_) for tuple_ in permutations(permutation_input)}
    for potential_anagram in all_permutations:
        potential_anagram_words = potential_anagram.split(' ')
        if all(word in language_words for word in potential_anagram_words):
            yield potential_anagram

def read_english_words():
    dict_path = Path('/usr/share/dict/words')
    with dict_path.open() as dict_file:
        dict_set = {line.rstrip() for line in dict_file}
    return dict_set
