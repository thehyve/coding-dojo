from contextlib import suppress


def _has_unknown_opt(args, schema):
    expecting_value = False
    for argument in args:
        if expecting_value:
            expecting_value = False
            continue
        if not argument.startswith('-'):
            continue
        argument = argument.lstrip('-')
        if argument not in schema:
            return True
        option_type = schema[argument]
        expecting_value = option_type != 'flag'

    return False

def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    if _has_unknown_opt(args, schema):
        raise ValueError()
    result = {}
    # make a list we can mutate internally
    unrecognised_args = list(args)
    for arg, arg_type in schema.items():
        darg = '-' + arg
        with suppress(ValueError):
            unrecognised_args.remove(darg)
        if arg_type == 'flag':
            result[arg] = darg in args
        elif arg_type == 'int':
            try:
                arg_index = args.index(darg)
            except ValueError:
                result[arg] = 0
            else:
                result[arg] = int(args[arg_index+1])
        elif arg_type == 'str':
            try:
                arg_index = args.index(darg)
            except ValueError:
                result[arg] = ''
            else:
                result[arg] = args[arg_index+1]

    # take all remaining arguments as positionals
    result.positional = unrecognised_args

    return result
