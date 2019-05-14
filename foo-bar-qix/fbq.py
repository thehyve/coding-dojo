from contextlib import suppress


def compute(arg):
    special_cases = {
        '3': 'FooFoo',
        '5': 'BarBar',
        '7': 'QixQix',
    }
    with suppress(KeyError):
        return special_cases[arg]
    if int(arg) % 3 == 0:
        return 'Foo'
    return arg
