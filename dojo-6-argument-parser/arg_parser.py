from contextlib import suppress
from collections import UserDict


def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    expecting_value = False
    for potential_opt in args:
        if expecting_value:
            expecting_value = False
            continue
        if not potential_opt.startswith('-'):
            continue
        potential_opt = potential_opt.lstrip('-')
        if potential_opt not in schema:
            raise ValueError()
        option_type = schema[potential_opt]
        expecting_value = option_type != 'flag'
# TODO: incorporate functionality below into
# refactor above
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
# TODO: incorporate logic above into refactoring
# above that

    # take all remaining arguments as positionals
    output = UserDict(parsed_opts)
    output.positional = unrecognised_args

    return output
