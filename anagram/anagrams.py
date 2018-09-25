from pathlib import Path
from itertools import permutations


def anagrams(word, n_words=1):
    spaces_to_add = (n_words-1)*' '
    word += spaces_to_add
    dict_path = Path('/usr/share/dict/words')
    all_permutations = {''.join(tuple_) for tuple_ in permutations(word)}

    with dict_path.open() as dict_file:
        dict_set = {line.rstrip() for line in dict_file}
        for potential_anagram in all_permutations:
            potential_anagram_words = potential_anagram.split(' ')
            if all(word in dict_set for word in potential_anagram_words):
                yield potential_anagram
