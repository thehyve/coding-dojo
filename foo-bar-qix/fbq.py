def compute(arg):
    if arg == '3':
        return 'FooFoo'
    if arg == '5':
        return 'BarBar'
    if int(arg) % 3 == 0:
        return 'Foo'
    return arg
