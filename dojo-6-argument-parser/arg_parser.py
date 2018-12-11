def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    if any(arg.lstrip('-') not in schema
            for arg
            in args
            if arg.startswith('-')):
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
    return result
