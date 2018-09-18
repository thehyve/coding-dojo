from pathlib import Path
from itertools import permutations

def anagrams(word):
    dict_path = Path('/usr/share/dict/words')
    all_permutations = {''.join(tuple_) for tuple_ in permutations(word)}
    with dict_path.open() as dict_file:
        for line in dict_file:
            line = line.rstrip()
            if line in all_permutations:
                yield line
