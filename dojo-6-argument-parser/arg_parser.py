def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    if any(arg.lstrip('-') not in schema
            for arg
            in args
            if arg.startswith('-')):
        raise ValueError
    result = {}
    for arg, arg_type in schema.items():
        if arg_type == 'flag':
            result[arg] = ('-' + arg) in args
        elif arg_type == 'int':
            arg_index = args.index('-' + arg)
            if arg_index == -1:
                result[arg] = 0
            else:
                result[arg] = int(args[arg_index+1])
    return result
