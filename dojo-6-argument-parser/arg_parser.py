from contextlib import suppress
from collections import UserDict


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
    parsed_opts = {}
    # make a list we can mutate internally
    unrecognised_args = list(args)
    for arg, arg_type in schema.items():
        darg = '-' + arg
        with suppress(ValueError):
            unrecognised_args.remove(darg)
        if arg_type == 'flag':
            parsed_opts[arg] = darg in args
        elif arg_type == 'int':
            try:
                arg_index = args.index(darg)
            except ValueError:
                parsed_opts[arg] = 0
            else:
                parsed_opts[arg] = int(args[arg_index+1])
        elif arg_type == 'str':
            try:
                arg_index = args.index(darg)
            except ValueError:
                parsed_opts[arg] = ''
            else:
                parsed_opts[arg] = args[arg_index+1]

    # take all remaining arguments as positionals
    output = UserDict(parsed_opts)
    output.positional = unrecognised_args

    return output
