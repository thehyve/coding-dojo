def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    if any(arg.lstrip('-') not in schema
            for arg
            in args
            if arg.startswith('-')):
        raise ValueError
    return {arg: ('-' + arg in args) for arg in schema}
