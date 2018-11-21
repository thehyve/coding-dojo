def parse_args(schema, args):
    """Parse the arguments according to the schema."""
    if any(arg.lstrip('-') not in schema for arg in args):
        raise ValueError
    if not args:
        return {key: False for key in schema}
    return {arg.lstrip('-'): arg.lstrip('-') in schema for arg in args}
