"""Traverses through the class hierarchy"""

def tree(cls):
    yield cls.__name__,0
    for sub_cls in cls.__subclasses__():
        yield sub_cls.__name__,1

def display(cls):
    for clsname,level in tree(cls):
        indent = ' ' * 4 * level
        print(f'{indent}{clsname}')

if __name__=='__main__':
    display(BaseException)