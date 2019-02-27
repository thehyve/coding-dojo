from contextlib import suppress
from collections import UserDict


def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    expecting_value = False
    parsed_opts = {
        flag: False 
        for flag, opt_type 
        in schema.items() 
        if opt_type == 'flag'}
    positionals = []
    for potential_opt in args:
        if expecting_value:
            # TODO Handle argument
            expecting_value = False
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
        expecting_value = option_type != 'flag'
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
    output.positional = positionals

    return output
