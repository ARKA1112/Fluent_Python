def tree(cls):
    yield cls.__name__,0
    yield from subtree(cls)


def subtree(cls):
    for sub_cls in cls.__subclasses__():
        yield sub_cls.__name__,1


def display(cls):
    for sub_cls, level in tree(cls):
        indent = ' ' * 4 * level
        print(f'{indent}{sub_cls}')


if __name__ == '__main__':
    display(BaseException)