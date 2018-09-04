from pathlib import Path
def anagrams(word):
    dict_path = Path('/usr/share/dict/words')
    with dict_path.open() as dict_file:
        if word not in (line.rstrip() for line in dict_file):
            raise StopIteration()
    return iter([word])
