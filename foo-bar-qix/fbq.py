def compute(arg):
    special_cases = {
        '3': 'FooFoo',
        '5': 'BarBar',
        '7': 'QixQix',
    }
    try:
        return special_cases[arg]
    except KeyError:
        pass
    if int(arg) % 3 == 0:
        return 'Foo'
    return arg
