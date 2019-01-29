def diamond(letter):
    start = ord('A')
    end = ord(letter)
    diff = end - start
    if diff == 0:
        return 'A'
    first_line = diff*' ' + 'A' + diff*' '
    return '\n'.join([ 
        first_line,
        _diamond_body(letter, diff),
        first_line])

def _diamond_body(letter, diff):
    letters = [chr(i) for i in range(ord('B'), ord(letter) + 1)]
    out = ''
    width = diff * 2 + 1
    for i, l in enumerate(letters):
        side_spaces = (diff - (i + 1)) * ' '
        midle_spaces = (width - 2 - len(side_spaces) * 2) * ' ' 
        out += side_spaces + l + midle_spaces + l + side_spaces 
        if i + 1 < len(letters):
            out += '\n'
    return out 
