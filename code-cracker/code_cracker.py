decryption_key = {
    '!': 'a',
    ')': 'b',
    '"': 'c',
    '(': 'd',
    '£': 'e',
    '*': 'f',
    '%': 'g',
    '&': 'h',
    '>': 'i',
    '<': 'j',
    '@': 'k',
    'a': 'l',
    'b': 'm',
    'c': 'n',
    'd': 'o',
    'e': 'p',
    'f': 'q',
    'g': 'r',
    'h': 's',
    'i': 't',
    'j': 'u',
    'k': 'v',
    'l': 'w',
    'm': 'x',
    'n': 'y',
    'o': 'z',
    ' ': ' ',
}

def decrypt(msg):
    return ''.join(map(lambda s: decryption_key[s], msg))

encryption_key = {v: k for k, v in decryption_key.items()}

def encrypt(msg):
    return ''.join(map(lambda s: encryption_key[s], msg))
