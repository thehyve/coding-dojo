def _has_unknown_opt(args, schema):
    return any(arg.lstrip('-') not in schema
            for arg
            in args
            if arg.startswith('-') and not arg[1:].isdigit()
            )

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
    return result
