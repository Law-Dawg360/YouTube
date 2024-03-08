import uuid

def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)


def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)
