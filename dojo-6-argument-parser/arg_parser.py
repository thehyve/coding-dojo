from contextlib import suppress
from collections import UserDict


DEFAULT_VALUES_BY_TYPE = {
    'flag': False,
    'str': '',
    'int': 0,
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
            opt_name, parse_value = expecting_value_for
            parsed_opts[opt_name] = parse_value(potential_opt)
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
            expecting_value_for = (
                potential_opt,
                lambda x: x
            )
        elif option_type == 'int':
            expecting_value_for = (potential_opt, int)
        else:
            expecting_value_for = option_type != 'flag'
    # take all remaining arguments as positionals
    output = UserDict(parsed_opts)
    output.positional = positionals

    return output
