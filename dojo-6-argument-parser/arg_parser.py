from contextlib import suppress
from collections import UserDict


DEFAULT_VALUES_BY_TYPE = {
    'flag': False,
    'str': '',
    'int': 0,
}

VALUE_PARSERS_BY_TYPE = {
    'str': lambda x: x,
    'int': int,
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
            opt_name, opt_type = expecting_value_for
            parse_value = VALUE_PARSERS_BY_TYPE[opt_type]
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
        else:
            expecting_value_for = potential_opt, option_type
    # take all remaining arguments as positionals
    output = UserDict(parsed_opts)
    output.positional = positionals

    return output
