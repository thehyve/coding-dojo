def _has_unknown_opt(args, schema):
    skip = False
    for option in args:
        if skip:
            skip = False
            continue
        if option[0] != '-':
            return True
        option = option.lstrip('-')
        if option not in schema:
            return True
        option_type = schema[option]
        skip = option_type != 'flag'

    return False

def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    if _has_unknown_opt(args, schema):
        raise ValueError()
    result = {}
    for arg, arg_type in schema.items():
        darg = '-' + arg
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

    return result
