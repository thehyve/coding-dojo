from pathlib import Path
from itertools import permutations


def anagrams(word, n_words=1):
    yield from get_anagrams_in_language(word, n_words, read_english_words())

def get_anagrams_in_language(word, n_words, language_words):
    all_permutations = collect_potential_anagrams(word, n_words)
    for potential_anagram in all_permutations:
        #potential_anagram_words = potential_anagram.split(' ')
        if all(word in language_words for word in potential_anagram):
            yield potential_anagram

def collect_potential_anagrams(word, n_words):
    """Get all permutations of 'word' split into 'n_words'"""
    spaces_to_add = (n_words-1)*' '
    permutation_input = word + spaces_to_add
    return {tuple(''.join(tuple_).split(' ')) for tuple_ in permutations(permutation_input)}

def read_english_words():
    dict_path = Path('/usr/share/dict/words')
    with dict_path.open() as dict_file:
        dict_set = {line.rstrip() for line in dict_file}
    return dict_set
