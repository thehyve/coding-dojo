from contextlib import suppress
from collections import UserDict


DEFAULT_VALUES_BY_TYPE = {
    'flag': False,
    'str': '',
}


def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    # assume opts for values not yet encountered
    parsed_opts = {
        # TODO Properly handle unsupported opt types
        opt: DEFAULT_VALUES_BY_TYPE.get(opt_type, None)
        for opt, opt_type
        in schema.items()
    }
    positionals = []
    expecting_value_for = None
    for potential_opt in args:
        if expecting_value_for:
            parsed_opts[expecting_value_for] = potential_opt
            expecting_value_for = None
            continue
        if not potential_opt.startswith('-'):
            positionals += potential_opt
            continue
        potential_opt = potential_opt.lstrip('-')
        if potential_opt not in schema:
            raise ValueError()
        option_type = schema[potential_opt]
        if option_type == 'flag':
            parsed_opts[potential_opt] = True
        elif option_type == 'str':
            expecting_value_for = potential_opt
        else:
            expecting_value_for = option_type != 'flag'
# TODO: incorporate functionality below into
# refactor above
    # make a list we can mutate internally
    for arg, arg_type in schema.items():
        darg = '-' + arg
        if arg_type == 'int':
            try:
                arg_index = args.index(darg)
            except ValueError:
                parsed_opts[arg] = 0
            else:
                parsed_opts[arg] = int(args[arg_index+1])
# TODO: incorporate logic above into refactoring
# above that

    # take all remaining arguments as positionals
    output = UserDict(parsed_opts)
    output.positional = positionals

    return output
